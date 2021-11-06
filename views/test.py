from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, \
    QGridLayout, QPushButton, QStackedWidget

from src.settings import TEST_START_LABEL, TEST_START_BUTTON, \
    TEST_START_LABEL_STYLE, TEST_RESULT_LABEL_STYLE, \
    TEST_RESULT_BUTTON_SAVE, TEST_RESULT_BUTTON_NEW, BUTTON_TEXT_STYLE, \
    TEST_TEST_BUTTON, TEST_TRY_COUNTER


class TestView(QWidget):
    """
    Этот класс верстает вкладку "Тест".
    Вкладка, в которой пользователь будет проходить тестирование.
    У этой вкладки есть три сценария:
    1. Старт (приглашение начать тест).
    2. Тест (сам тест с возможностью выбора фигуры).
    3. Результат (результат теста с возможностью его сохранения).
    """

    def __init__(self):
        """
        Этот метод реализует наполнение виджета QStackedWidget.
        В данном виджете хранятся все сценарии.
        По умолчанию изначальный сценарии — "старт".
        """
        super().__init__()

        self.main_screen = QVBoxLayout(self)

        self.start = QWidget()
        self.test = QWidget()
        self.result = QWidget()

        self.fill_start_window()
        self.fill_test_window()
        self.fill_result_window()

        self.window_stage = QStackedWidget(self)
        self.window_stage.addWidget(self.start)
        self.window_stage.addWidget(self.test)
        self.window_stage.addWidget(self.result)
        self.window_stage.setCurrentIndex(0)

        self.main_screen.addWidget(self.window_stage)

    def fill_start_window(self):
        """
        Этот метод верстает сценарий "старт".
        """
        self.start_layout = QVBoxLayout(self)
        self.start_label = QLabel(TEST_START_LABEL, self)
        self.start_label.setStyleSheet(TEST_START_LABEL_STYLE)
        self.start_grid = QGridLayout(self)
        self.start_button = QPushButton(TEST_START_BUTTON, self)

        self.start_button.setMaximumHeight(80)
        self.start_button.setStyleSheet(BUTTON_TEXT_STYLE)

        self.start_grid.setColumnStretch(0, 1)
        self.start_grid.setColumnStretch(2, 1)
        self.start_grid.setRowStretch(0, 1)
        self.start_grid.setRowStretch(3, 1)
        self.start_grid.setRowMinimumHeight(2, 120)

        self.start_grid.addWidget(self.start_label, 1, 1)
        self.start_grid.addWidget(self.start_button, 2, 1)

        self.start_layout.addLayout(self.start_grid)
        self.start.setLayout(self.start_layout)

    def fill_test_window(self):
        """
        Этот метод верстает сценарий "тест".
        """
        self.test_layout = QVBoxLayout(self)
        self.test_grid = QGridLayout(self)

        self.test_counter = QLabel(f'{TEST_TRY_COUNTER}')

        self.test_image_left = QLabel(self)
        self.test_image_right = QLabel(self)

        self.test_button_left = QPushButton(TEST_TEST_BUTTON, self)
        self.test_button_right = QPushButton(TEST_TEST_BUTTON, self)

        self.test_button_left.setMinimumSize(160, 80)
        self.test_button_left.setStyleSheet(BUTTON_TEXT_STYLE)
        self.test_button_right.setMinimumSize(160, 80)
        self.test_button_right.setStyleSheet(BUTTON_TEXT_STYLE)

        self.test_grid.setColumnStretch(0, 1)
        self.test_grid.setColumnStretch(2, 1)
        self.test_grid.setColumnStretch(4, 1)
        self.test_grid.setRowStretch(0, 1)
        self.test_grid.setRowStretch(2, 1)
        self.test_grid.setRowStretch(4, 1)

        self.test_grid.addWidget(self.test_counter, 0, 5)
        self.test_grid.addWidget(self.test_image_left, 1, 1)
        self.test_grid.addWidget(self.test_image_right, 1, 3)

        self.test_grid.addWidget(self.test_button_left, 3, 1)
        self.test_grid.addWidget(self.test_button_right, 3, 3)

        self.test_layout.addLayout(self.test_grid)
        self.test.setLayout(self.test_layout)

    def fill_result_window(self):
        """
        Этот метод верстает сценарий "результат".
        """
        self.result_layout = QVBoxLayout(self)
        self.result_grid = QGridLayout(self)

        self.result_label = QLabel(self)
        self.result_label.setStyleSheet(TEST_RESULT_LABEL_STYLE)

        self.result_button_save = QPushButton(TEST_RESULT_BUTTON_SAVE, self)
        self.result_button_new = QPushButton(TEST_RESULT_BUTTON_NEW, self)

        self.result_button_save.setMinimumSize(160, 60)
        self.result_button_save.setStyleSheet(BUTTON_TEXT_STYLE)
        self.result_button_new.setMinimumSize(160, 60)
        self.result_button_new.setStyleSheet(BUTTON_TEXT_STYLE)

        self.result_grid.setColumnStretch(0, 1)
        self.result_grid.setRowStretch(0, 1)
        self.result_grid.setRowStretch(1, 1)

        self.result_grid.addWidget(self.result_label, 0, 0, 1, 2)
        self.result_grid.addWidget(self.result_button_new, 2, 1)
        self.result_grid.addWidget(self.result_button_save, 2, 2)

        self.result_layout.addLayout(self.result_grid)
        self.result.setLayout(self.result_layout)
