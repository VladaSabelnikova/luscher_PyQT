from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QPushButton, \
    QGridLayout

from src.settings import DATA_BASE_TYPE, \
    DB_NAME_PATH, BUTTON_TEXT_STYLE, ANALYZER_BUTTON_ADD, \
    ANALYZER_BUTTON_UPDATE, \
    ANALYZER_BUTTON_DELETE, ANALYZER_DB_TABLE, \
    ANALYZER_BUTTON_EXPORT, ANALYZER_BUTTON_IMPORT


class AnalyzerView(QWidget):
    """
        Этот класс верстает вкладку "Настройки".
        Вкладка, в которой можно взаимодействовать с таблицей analyzer.
        Она нужна для изменения настроек анализа теста.
        """

    def __init__(self):
        """
        Этот метод верстает "Настройки".
        """
        super().__init__()
        self.analyzer_layout = QVBoxLayout(self)
        self.analyzer_grid = QGridLayout(self)

        self.analyzer_button_export = QPushButton(ANALYZER_BUTTON_EXPORT, self)
        self.analyzer_button_import = QPushButton(ANALYZER_BUTTON_IMPORT, self)
        self.analyzer_button_add = QPushButton(ANALYZER_BUTTON_ADD, self)
        self.analyzer_button_update = QPushButton(ANALYZER_BUTTON_UPDATE, self)
        self.analyzer_button_delete = QPushButton(ANALYZER_BUTTON_DELETE, self)

        self.analyzer_button_export.setMinimumSize(160, 60)
        self.analyzer_button_export.setStyleSheet(BUTTON_TEXT_STYLE)

        self.analyzer_button_import.setMinimumSize(160, 60)
        self.analyzer_button_import.setStyleSheet(BUTTON_TEXT_STYLE)

        self.analyzer_button_add.setMinimumSize(160, 60)
        self.analyzer_button_add.setStyleSheet(BUTTON_TEXT_STYLE)

        self.analyzer_button_update.setMinimumSize(160, 60)
        self.analyzer_button_update.setStyleSheet(BUTTON_TEXT_STYLE)

        self.analyzer_button_delete.setMinimumSize(160, 60)
        self.analyzer_button_delete.setStyleSheet(BUTTON_TEXT_STYLE)

        self.analyzer_grid.addWidget(self.analyzer_button_export, 0, 0)
        self.analyzer_grid.addWidget(self.analyzer_button_import, 0, 1)
        self.analyzer_grid.addWidget(self.analyzer_button_add, 0, 2)
        self.analyzer_grid.addWidget(self.analyzer_button_update, 0, 3)
        self.analyzer_grid.addWidget(self.analyzer_button_delete, 0, 4)

        self.display_analyzer()

        self.analyzer_layout.addLayout(self.analyzer_grid)

    def display_analyzer(self):
        """
        Этот метод отображает содержимое таблицы analyzer в виджете QTableView
        и добавляет его в главный виджет (analyzer_layout).
        """
        self.db = QSqlDatabase.addDatabase(DATA_BASE_TYPE)
        self.db.setDatabaseName(DB_NAME_PATH)
        self.db.open()

        self.analyzer_data_base = QTableView(self)
        self.analyzer_model = QSqlTableModel(self, self.db)
        self.analyzer_model.setTable(ANALYZER_DB_TABLE)
        self.analyzer_model.select()

        self.analyzer_data_base.setModel(self.analyzer_model)
        self.analyzer_data_base.setColumnWidth(0, 50)
        self.analyzer_data_base.setColumnWidth(1, 200)
        self.analyzer_data_base.setColumnWidth(2, 530)

        self.analyzer_layout.addWidget(self.analyzer_data_base)
