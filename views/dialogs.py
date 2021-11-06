from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, \
    QGridLayout, QLineEdit, QPlainTextEdit, QMessageBox, QFileDialog

from src.settings import DIALOG_UPDATE_AND_ADD_RESULT_CODE_TEXT, \
    DIALOG_UPDATE_AND_ADD_DESCRIPTION_TEXT, DIALOG_UPDATE_AND_ADD_BUTTON_SAVE, \
    PLACEHOLDER_RESULT_CODE, PLACEHOLDER_DESCRIPTION, BUTTON_TEXT_STYLE, \
    DIALOG_UPDATE_AND_ADD_TITLE, DIALOG_DELETE_CONFIRMATION_TEXT, \
    DIALOG_DELETE_CONFIRMATION_TITLE, DIALOG_VIEW_TITLE, DIALOG_EXPORT_TITLE, \
    DIALOG_EXPORT_EXTENSION, DIALOG_EXPORT_PATH_TO_DB, DIALOG_IMPORT_TITLE, \
    DIALOG_IMPORT_EXTENSION, DIALOG_IMPORT_PATH_TO_DB, \
    DIALOG_VIEW_STYLE, DIALOG_BUTTON_DELETE, \
    DIALOG_BUTTON_CANCEL, DIALOG_DELETE_STYLE, DIALOG_MESSAGE_STYLE, \
    DIALOG_INFORMATION_STYLE


class DialogBoxes(QDialog):
    """
    Этот класс верстает диалоги.
    В нём создаются все диалоги и окна сообщений,
    которые используются в программе.
    """

    def __init__(self):
        """
        Этот метод в момент инициализации создает маркер,
        благодаря которому в дальнейшем
        можно будет отслеживать номер нажатой кнопки в диалогах.
        """
        super().__init__()
        self.clicked_button_code = 0

    def dialog_update_and_add(self, result_code='', description=''):
        """
        Этот метод верстает диалог добавления/изменения
        содержимого базы данных.
        Важный момент — он универсально подходит как и для добавления в базу,
        так и для изменения базы.
        """
        dialog = QDialog()
        dialog.setWindowTitle(DIALOG_UPDATE_AND_ADD_TITLE)
        dialog.setMinimumSize(600, 400)
        grid_layout = QGridLayout(dialog)

        result_code_input = QLineEdit(result_code)
        result_code_input.setMaximumHeight(50)
        result_code_input.setPlaceholderText(PLACEHOLDER_RESULT_CODE)
        result_code_label = QLabel(DIALOG_UPDATE_AND_ADD_RESULT_CODE_TEXT)

        description_input = QPlainTextEdit(description)
        description_input.setPlaceholderText(PLACEHOLDER_DESCRIPTION)
        description_label = QLabel(DIALOG_UPDATE_AND_ADD_DESCRIPTION_TEXT)

        button_save = QPushButton(DIALOG_UPDATE_AND_ADD_BUTTON_SAVE)
        button_save.setMinimumSize(160, 60)
        button_save.setStyleSheet(BUTTON_TEXT_STYLE)
        button_save.clicked.connect(dialog.accept)

        grid_layout.setRowStretch(4, 1)
        grid_layout.setRowStretch(1, 1)

        grid_layout.addWidget(result_code_label, 1, 0)
        grid_layout.addWidget(result_code_input, 1, 1, 1, 3)

        grid_layout.addWidget(description_label, 3, 0)
        grid_layout.addWidget(description_input, 3, 1, 2, 3)
        grid_layout.addWidget(button_save, 5, 3)

        # В случае нажатия на кнопку "Сохранить" диалог возвращает данные.
        if dialog.exec_():
            return result_code_input.text(), description_input.toPlainText()
        else:
            return None

    def dialog_export(self):
        """
        Этот метод верстает стандартный диалог сохранения (экспорта) файла.
        """
        file_path = QFileDialog.getSaveFileName(
            self,
            DIALOG_EXPORT_TITLE,
            filter=DIALOG_EXPORT_EXTENSION,
            directory=DIALOG_EXPORT_PATH_TO_DB
        )
        return file_path

    def dialog_import(self):
        """
        Этот метод верстает стандартный диалог импорта файла.
        """
        file_path = QFileDialog.getOpenFileName(
            self,
            DIALOG_IMPORT_TITLE,
            filter=DIALOG_IMPORT_EXTENSION,
            directory=DIALOG_IMPORT_PATH_TO_DB
        )
        return file_path

    def dialog_view(self, description, data):
        """
        Этот метод верстает окно сообщение просмотра (в нашем случае базы).
        Он создает стандартное окно "информация",
        в котором будут находится данные из history.
        Вызывается всякий раз,
        когда пользователь хочет подробно просмотреть содержимое строки базы.
        Его задача красиво и читабельно показать содержимое ячейки.
        """
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)

        dialog.setText(f'\n{data}\n\n{description}\n')
        dialog.setWindowTitle(DIALOG_VIEW_TITLE)
        dialog.setStyleSheet(f'{DIALOG_VIEW_STYLE} {BUTTON_TEXT_STYLE}')
        dialog.window().setStyleSheet(DIALOG_INFORMATION_STYLE)

        button_delete = QPushButton(DIALOG_BUTTON_DELETE)
        button_cancel = QPushButton(DIALOG_BUTTON_CANCEL)

        dialog.addButton(button_delete, QMessageBox.YesRole)
        dialog.addButton(button_cancel, QMessageBox.NoRole)

        button_cancel.clicked.connect(self.cancel_button_clicked)
        button_delete.clicked.connect(self.action_button_clicked)

        dialog.exec_()
        return self.clicked_button_code

    def dialog_delete_confirmation(self):
        """
        Этот метод верстает окно сообщение предупреждения.
        Он создает стандартное окно "критический",
        которое будет вызываться всякий раз,
        когда пользователь захочет удалить строку из базы.
        Его задача получить подтверждение/отмену удаления.
        """
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Critical)

        dialog.setText(DIALOG_DELETE_CONFIRMATION_TEXT)
        dialog.setWindowTitle(DIALOG_DELETE_CONFIRMATION_TITLE)
        dialog.setStyleSheet(f'{DIALOG_DELETE_STYLE} {BUTTON_TEXT_STYLE}')
        dialog.window().setStyleSheet(DIALOG_MESSAGE_STYLE)

        button_delete = QPushButton(DIALOG_BUTTON_DELETE)
        button_cancel = QPushButton(DIALOG_BUTTON_CANCEL)

        dialog.addButton(button_delete, QMessageBox.YesRole)
        dialog.addButton(button_cancel, QMessageBox.NoRole)

        button_cancel.clicked.connect(self.cancel_button_clicked)
        button_delete.clicked.connect(self.action_button_clicked)

        dialog.exec_()
        return self.clicked_button_code

    def cancel_button_clicked(self):
        """
        Этот метод заменяет значение маркера при нажатии на кнопку "закрыть".
        """
        self.clicked_button_code = 0

    def action_button_clicked(self):
        """
        Этот метод заменяет значение маркера при нажатии на кнопку,
        которая генерирует какое-либо действие.
        """
        self.clicked_button_code = 1
