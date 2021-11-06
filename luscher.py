import sys

from PyQt5.QtWidgets import QHBoxLayout, QTabWidget, QMainWindow, \
    QApplication
from PyQt5.QtWidgets import QWidget

from models.analyzer import AnalyzerModel
from models.history import HistoryModel
from models.test import TestModel
from src.settings import BUTTON_TEXT_STYLE, TAB_TEST, TAB_HISTORY, TAB_ANALYZER


class UserInterface(QWidget):
    """
    Этот класс создаёт вкладки (Тест, История, Настройки).
    """

    def __init__(
        self
    ):
        """
        Этот метод выполняет вёрстку вкладок.
        """
        super().__init__()

        self.main_layout = QHBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.tabs.setStyleSheet(BUTTON_TEXT_STYLE)

        self.tab_0 = TestModel()
        self.tab_1 = HistoryModel()
        self.tab_2 = AnalyzerModel()

        self.tabs.addTab(self.tab_0, TAB_TEST)
        self.tabs.addTab(self.tab_1, TAB_HISTORY)
        self.tabs.addTab(self.tab_2, TAB_ANALYZER)
        self.main_layout.addWidget(self.tabs)

        self.tabs.currentChanged.connect(self.refresh_screen)

    def refresh_screen(self):
        """
        Этот метод обновляет вьюху history в том случае,
        если пользователь нажал на вкладку "История".
        """
        if self.tabs.currentIndex() == 1:
            self.tab_1.history_model.select()


class Window(QMainWindow):
    """
    Этот класс создаёт главное окно.
    """

    def __init__(self):
        super().__init__()

        self.setMinimumSize(850, 800)

        self.setCentralWidget(UserInterface())
        self.setWindowTitle('Тест Люшера-Деллингер')


def except_hook(cls, exception, traceback):
    """
    Эта функция выводит в консоль ошибки (баги).
    """
    sys.__excepthook__(cls, exception, traceback)


def main():
    """
    Эта функция запускает процесс отображения главного окна.
    """
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
