import datetime
import difflib
import sqlite3
from itertools import product
from random import choice

from PIL import Image, ImageDraw
from PyQt5.QtGui import QPixmap

from src.settings import COLORS, SHAPES, PATH_TO_TMP_IMAGE_LEFT, \
    PATH_TO_TMP_IMAGE_RIGHT, TEST_TRY_COUNTER, DB_NAME_PATH
from views.test import TestView


class TestModel(TestView):
    """
    Этот класс описывает логику работы вкладки "Тест".
    Следовательно описывает логику работы трех сценариев теста.
    Стоит обратить внимание, что цвета и фигуры,
    используемые в тесте — записаны в src/settings.py
    """

    def __init__(self):
        """
        Этот метод привязывает к кнопкам всех сценариев события.
        """
        super().__init__()
        self.start_button.clicked.connect(self.start_test)
        self.test_button_left.clicked.connect(self.test_left_shape_selected)
        self.test_button_right.clicked.connect(self.test_right_shape_selected)
        self.result_button_save.clicked.connect(self.result_save)
        self.result_button_new.clicked.connect(self.result_new)

    def start_test(self):
        """
        Этот метод осуществляет подготовительные мероприятия
        для валидной работы теста:
            * Обнуляет результаты теста.
            * Обнуляет счетчик пройденных тестов.
            * Меняет сценарий на "тест".
            * Генерирует все пары фигур в рандомном режиме.
            Под парами мы понимаем номер цвета и тип фигуры.
            * Достаёт первую пару фигур.

        Важный момент!!!
        Генерация пар фигур гарантирует:
            * В тест попадут все типы фигур
            * У каждого типа фигур будут все виды цветов.
        """
        self.json_result = {
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
            '7': [],
            '8': []
        }
        self.try_counter = 0
        self.test_update_try_counter()
        self.window_stage.setCurrentIndex(1)
        self.colored_shapes = list(set(product(COLORS.keys(), SHAPES.keys())))
        for _ in range(TEST_TRY_COUNTER * 2 - len(self.colored_shapes)):
            self.colored_shapes.append(choice(self.colored_shapes))
        self.new_shapes()

    def test_left_shape_selected(self):
        """
        Этот метод — событие.
        Оно вызывается всякий раз, когда пользователь выбрал фигуру слева.
        Его задача записать выбор в результат теста
        и сгенерировать новую пару фигур.
        """
        self.test_update_try_counter()
        left = self.left_choice
        self.json_result[left[0]].append(left[1])
        if self.try_counter > TEST_TRY_COUNTER:
            self.test_diagnosis()
        else:
            self.new_shapes()

    def test_right_shape_selected(self):
        """
        Этот метод — событие.
        Оно вызывается всякий раз, когда пользователь выбрал фигуру справа.
        Его задача записать выбор в результат теста
        и сгенерировать новую пару фигур.
        """
        self.test_update_try_counter()
        right = self.right_choice
        self.json_result[right[0]].append(right[1])
        if self.try_counter > TEST_TRY_COUNTER:
            self.test_diagnosis()
        else:
            self.new_shapes()

    def test_diagnosis(self):
        """
        Этот метод выводит вердикт теста на экран.
        Он соотносит результаты теста с таблицей analyzer и,
        с помощью difflib, выясняет какой из диагнозов больше всех похож на
        результаты теста, после чего этот диагноз выводит на экран.
        """
        self.window_stage.setCurrentIndex(2)
        value_user = self.test_examination()
        self.possible_diagnoses = []
        con = sqlite3.connect(DB_NAME_PATH)
        cur = con.cursor()
        select = 'SELECT * ' \
                 'FROM analyzer'
        result = cur.execute(select).fetchall()
        con.close()
        for elem in result:
            id, value_db, description = elem
            verdict = self.test_similarity(value_user, value_db)
            self.possible_diagnoses.append([description, verdict, id])
        self.possible_diagnoses.sort(key=lambda s: s[1], reverse=True)
        self.result_label.setText(f'{self.possible_diagnoses[0][0]}')

    def test_examination(self):
        """
        Этот метод приводит результат теста в правильный вид:
            * Сначала цвета, потом типы фигур
            * По убыванию частоты нажатий цветов
            * По убыванию частоты нажатий типов фигур
            * В конец добавляются те цвета и фигуры, которые пользователь
            вообще не нажимал (они тоже в ходят в анализ).
        """
        colors = []
        transit = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0
        }
        for color, shapes in self.json_result.items():
            colors.append([color, len(shapes)])
            for shape in shapes:
                transit[shape] += 1
        shapes = []
        for shape, rating in transit.items():
            shapes.append([shape, rating])
        colors.sort(key=lambda s: s[1])
        shapes.sort(key=lambda s: s[1])
        color = ''.join([elem[0] for elem in colors])
        shape = ''.join([elem[0] for elem in shapes])
        result = color + shape
        return result

    def test_similarity(self, value_user, value_db):
        """
        Этот метод позволяет выяснить коэффициент
        похожести результатов теста с возможными диагнозами
        из таблицы analyzer.
        """
        matcher = difflib.SequenceMatcher(None, value_user, value_db)
        return matcher.ratio()

    def test_update_try_counter(self):
        """
        Этот метод обновляет счет (номер текущей пары).
        Например: 1/30, 2/30 ....
        """
        self.try_counter += 1
        self.test_counter.setText(f'{self.try_counter}/{TEST_TRY_COUNTER}')

    def new_shapes(self):
        """
        Этот метод создает два файла png
        Вызывается всякий раз, когда мы создаём новую пару картинок.
        Важный момент!!!
        Гарантируется, что картинки не будут одинаковыми.
        """
        try:
            left = self.colored_shapes.pop()
            right = self.colored_shapes.pop()
            while left == right:
                self.colored_shapes.append(right)
                right = self.colored_shapes.pop(0)
            self.painter(*left, PATH_TO_TMP_IMAGE_LEFT)
            self.painter(*right, PATH_TO_TMP_IMAGE_RIGHT)
        except IndexError:
            left, right = tuple(), tuple()
        self.new_picture()
        self.left_choice, self.right_choice = left, right

    def new_picture(self):
        """
        Этот метод отображает сгенерированные изображения на экране.
        """
        self.pixmap_left = QPixmap(PATH_TO_TMP_IMAGE_LEFT)
        self.pixmap_right = QPixmap(PATH_TO_TMP_IMAGE_RIGHT)
        self.test_image_left.setPixmap(self.pixmap_left)
        self.test_image_right.setPixmap(self.pixmap_right)

    def painter(self, color, shape, file_name):
        """
        Этот метод, с помощью PIL, создает (рисует) картинку.
        Тут идет проверка на тип фигуры и в зависимости от этого рисуется.
        """
        new_image = Image.new("RGB", (300, 300), (255, 255, 255))
        draw = ImageDraw.Draw(new_image)
        shape_type = SHAPES[shape]
        fill_color = COLORS[color]

        if shape_type == 'polygon':
            draw.polygon((150, 0, 300, 300, 0, 300), fill=fill_color)
        elif shape_type == 'ellipse':
            draw.ellipse((0, 0, 300, 300), fill=fill_color)
        elif shape_type == 'square':
            draw.line((0, 150, 300, 150), fill=fill_color, width=300)
        elif shape_type == 'rectangle':
            draw.line((0, 150, 300, 150), fill=fill_color, width=180)
        elif shape_type == 'multiline':
            draw.line(
                (
                    200, 10,
                    290, 50,
                    150, 25,
                    290, 90,
                    50, 75,
                    290, 200,
                    30, 150,
                    150, 290,
                    45, 275
                ),
                fill=fill_color,
                width=15,
                joint="curve"
            )
        new_image.save(file_name, 'PNG')

    def result_save(self):
        """
        Этот метод добавляет результат тестирования в таблицу history.
        Запускается всякий раз, когда нажата кнопка "Сохранить".
        """
        con = sqlite3.connect(DB_NAME_PATH)
        cur = con.cursor()
        date = f'{datetime.datetime.now()}'
        date = date.split('.')[0]
        insert = f'INSERT INTO history (result, updated_at) ' \
                 f'VALUES ({self.possible_diagnoses[0][2]}, "{date}")'

        cur.execute(insert)
        con.commit()
        con.close()
        self.window_stage.setCurrentIndex(0)

    def result_new(self):
        self.window_stage.setCurrentIndex(0)
