import sqlite3

from src.settings import DB_NAME_PATH
from views.dialogs import DialogBoxes
from views.history import HistoryView


class HistoryModel(HistoryView, DialogBoxes):
    """
    Этот класс описывает логику работы вкладки "История".
    """

    def __init__(self):
        """
        Этот метод привязывает к кнопкам данной вкладки события.
        """
        super().__init__()
        self.history_button_delete.clicked.connect(self.history_delete)
        self.history_button_view.clicked.connect(self.history_view)

    def history_delete(self):
        """
        Этот метод удаляет строку таблицы history,
        предварительно вызвав окно сообщения.
        """
        do_delete = self.dialog_delete_confirmation()
        row = self.history_data_base.currentIndex().row()
        id = self.history_model.index(row, 0).data()
        if do_delete:
            con = sqlite3.connect(DB_NAME_PATH)
            cur = con.cursor()
            delete = f'DELETE FROM history WHERE id={id}'

            cur.execute(delete)
            con.commit()
            con.close()
            self.history_model.select()

    def history_view(self):
        """
        Этот метод позволяет просмотреть строку таблицы history,
        вызвав окно сообщения.
        """
        row = self.history_data_base.currentIndex().row()
        foreign_key = self.history_model.index(row, 1).data()
        data = self.history_model.index(row, 2).data()
        if foreign_key:

            con = sqlite3.connect(DB_NAME_PATH)
            cur = con.cursor()
            select = f'SELECT description ' \
                     f'FROM analyzer ' \
                     f'WHERE id = {foreign_key}'

            description, = cur.execute(select).fetchone()
            con.close()
            if self.dialog_view(description, data):
                self.history_delete()
