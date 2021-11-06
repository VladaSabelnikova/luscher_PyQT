import csv
import sqlite3

from src.settings import DB_NAME_PATH
from views.analyzer import AnalyzerView
from views.dialogs import DialogBoxes


class AnalyzerModel(AnalyzerView, DialogBoxes):
    """
    Этот класс описывает логику работы вкладки "Настройки".
    """
    def __init__(self):
        """
        Этот метод привязывает к кнопкам данной вкладки события.
        """
        super().__init__()
        self.analyzer_button_add.clicked.connect(self.analyzer_add)
        self.analyzer_button_delete.clicked.connect(self.analyzer_delete)
        self.analyzer_button_import.clicked.connect(self.analyzer_import)
        self.analyzer_button_export.clicked.connect(self.analyzer_export)
        self.analyzer_button_update.clicked.connect(self.analyzer_update)

    def analyzer_add(self):
        """
        Этот метод добавляет строку таблицы analyzer,
        предварительно вызвав диалоговое окно.
        """
        do_add = self.dialog_update_and_add()
        if do_add:
            code, desc = do_add
            con = sqlite3.connect(DB_NAME_PATH)
            cur = con.cursor()
            insert = f'INSERT INTO analyzer (result_code, description) ' \
                     f'VALUES ("{code}", "{desc}")'

            cur.execute(insert)
            con.commit()
            con.close()
            self.analyzer_model.select()

    def analyzer_delete(self):
        """
        Этот метод удаляет строку таблицы analyzer,
        предварительно вызвав окно сообщения.
        """
        do_delete = self.dialog_delete_confirmation()
        row = self.analyzer_data_base.currentIndex().row()
        id = self.analyzer_model.index(row, 0).data()
        if do_delete and id:
            con = sqlite3.connect(DB_NAME_PATH)
            cur = con.cursor()
            delete = f'DELETE FROM analyzer WHERE id={id}'

            cur.execute(delete)
            con.commit()
            con.close()
            self.analyzer_model.select()

    def analyzer_export(self):
        """
        Этот метод экспортирует таблицу analyzer в виде csv,
        предварительно вызвав диалоговое окно.
        """
        file_path, *_ = self.dialog_export()
        if file_path:
            con = sqlite3.connect(DB_NAME_PATH)
            cur = con.cursor()
            select = f'SELECT * FROM analyzer'

            result = cur.execute(select).fetchall()
            con.close()

            with open(file_path, 'w', newline='') as export_file:
                if result:
                    sqlite_to_csv = csv.writer(
                        export_file,
                        delimiter=';',
                        quotechar='"',
                        quoting=csv.QUOTE_ALL
                    )
                    for row in result:
                        out = [str(elem) for elem in row]
                        sqlite_to_csv.writerow(out)

    def analyzer_import(self):
        """
        Этот метод импортирует csv файл,
        предварительно вызвав диалоговое окно.
        """
        file_path, *_ = self.dialog_import()
        if file_path:
            con = sqlite3.connect(DB_NAME_PATH)
            cur = con.cursor()
            select_id = f'SELECT id FROM analyzer'

            all_id = []
            for elem in cur.execute(select_id).fetchall():
                all_id.append(*elem)
            con.close()
            with open(file_path) as csv_file:
                reader = csv.reader(csv_file, delimiter=';', quotechar='"')
                for row in reader:
                    id, result_code, description = row
                    if int(id) not in all_id:
                        con = sqlite3.connect(DB_NAME_PATH)
                        cur = con.cursor()
                        insert = f'INSERT INTO analyzer(' \
                                 f'result_code,' \
                                 f' description' \
                                 f') ' \
                                 f'VALUES ("{result_code}", "{description}")'

                        cur.execute(insert)
                        con.commit()
                        con.close()
            self.analyzer_model.select()

    def analyzer_update(self):
        """
        Этот метод обновляет строку таблицы analyzer,
        предварительно вызвав диалоговое окно.
        """
        row = self.analyzer_data_base.currentIndex().row()
        id = self.analyzer_model.index(row, 0).data()
        code = self.analyzer_model.index(row, 1).data()
        desc = self.analyzer_model.index(row, 2).data()
        do_update = self.dialog_update_and_add(
            result_code=code,
            description=desc
        )
        if do_update:
            code, desc = do_update
            con = sqlite3.connect(DB_NAME_PATH)
            cur = con.cursor()
            update = f'UPDATE analyzer ' \
                     f'SET result_code="{code}", description="{desc}" ' \
                     f'WHERE id={id}'

            cur.execute(update)
            con.commit()
            con.close()
            self.analyzer_model.select()
