from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QPushButton, \
    QGridLayout

from src.settings import DATA_BASE_TYPE, \
    DB_NAME_PATH, HISTORY_DB_TABLE, BUTTON_TEXT_STYLE, HISTORY_BUTTON_VIEW, \
    HISTORY_BUTTON_DELETE


class HistoryView(QWidget):
    """
    Этот класс верстает вкладку "История".
    Вкладка, в которой пользователь сможет просматривать свои результаты
    и удалять их (если они ему не понравились 🙂).
    """

    def __init__(self):
        """
        Этот метод верстает "Историю".
        """
        super().__init__()
        self.history_layout = QVBoxLayout(self)
        self.history_grid = QGridLayout(self)

        self.history_button_view = QPushButton(HISTORY_BUTTON_VIEW, self)
        self.history_button_delete = QPushButton(HISTORY_BUTTON_DELETE, self)

        self.history_button_view.setMinimumSize(160, 60)
        self.history_button_view.setStyleSheet(BUTTON_TEXT_STYLE)
        self.history_button_delete.setMinimumSize(160, 60)
        self.history_button_delete.setStyleSheet(BUTTON_TEXT_STYLE)

        self.history_grid.setColumnStretch(0, 1)

        self.history_grid.addWidget(self.history_button_delete, 0, 1)
        self.history_grid.addWidget(self.history_button_view, 0, 2)

        self.display_history()

        self.history_layout.addLayout(self.history_grid)

    def display_history(self):
        """
        Этот метод отображает содержимое таблицы history
        в виджете QTableView и добавляет его в главный виджет (history_layout).
        """
        self.db = QSqlDatabase.addDatabase(DATA_BASE_TYPE)
        self.db.setDatabaseName(DB_NAME_PATH)
        self.db.open()

        self.history_data_base = QTableView(self)
        self.history_model = QSqlTableModel(self, self.db)
        self.history_model.setTable(HISTORY_DB_TABLE)
        self.history_model.select()

        self.history_data_base.setModel(self.history_model)

        self.history_data_base.setColumnWidth(0, 50)
        self.history_data_base.setColumnWidth(1, 200)
        self.history_data_base.setColumnWidth(2, 530)

        self.history_layout.addWidget(self.history_data_base)
