"""
Этот файл содержит в себе все константные переменные,
которые используются в приложении.
"""

COLORS = {
    '1': (0, 0, 204),
    '2': (0, 180, 180),
    '3': (204, 51, 0),
    '4': (255, 236, 7),
    '5': (132, 0, 217),
    '6': (111, 61, 13),
    '7': (0, 0, 0),
    '8': (135, 135, 135)
}

SHAPES = {
    'A': 'polygon',
    'B': 'ellipse',
    'C': 'square',
    'D': 'rectangle',
    'E': 'multiline'
}

PATH_TO_TMP_IMAGE_LEFT = 'tmp/left.png'
PATH_TO_TMP_IMAGE_RIGHT = 'tmp/right.png'

TEST_START_LABEL = 'Нажмите "Старт" по готовности.'
TEST_START_LABEL_STYLE = 'font-size: 20px;'
TEST_START_BUTTON = 'Старт'

TEST_RESULT_LABEL_STYLE = 'font-size: 20px;'
TEST_RESULT_BUTTON_NEW = 'Новый тест'
TEST_RESULT_BUTTON_SAVE = 'Сохранить'

TEST_TEST_BUTTON = 'Эта'

BUTTON_TEXT_STYLE = 'font-size: 20px;'
TEST_TRY_COUNTER = 30

DATA_BASE_TYPE = 'QSQLITE'
DB_NAME_PATH = 'src\luscher.sqlite'
HISTORY_DB_TABLE = 'history'

HISTORY_BUTTON_DELETE = 'Удалить'
HISTORY_BUTTON_VIEW = 'Просмотр'

ANALYZER_BUTTON_DELETE = 'Удалить'
ANALYZER_BUTTON_ADD = 'Добавить'
ANALYZER_BUTTON_UPDATE = 'Изменить'
ANALYZER_BUTTON_EXPORT = 'Экспорт'
ANALYZER_BUTTON_IMPORT = 'Импорт'
ANALYZER_DB_TABLE = 'analyzer'

DIALOG_DELETE_CONFIRMATION_TEXT = '\n\nВы действительно хотите удалить?\n\n'
DIALOG_DELETE_CONFIRMATION_BUTTON = 'Удалить'
DIALOG_DELETE_CONFIRMATION_TITLE = 'Подтвердите удаление'

DIALOG_UPDATE_AND_ADD_RESULT_CODE_TEXT = 'Код результата:'
DIALOG_UPDATE_AND_ADD_DESCRIPTION_TEXT = 'Описание:'
DIALOG_UPDATE_AND_ADD_BUTTON_SAVE = 'Сохранить'
DIALOG_UPDATE_AND_ADD_TITLE = 'Добавить/Изменить запись'

PLACEHOLDER_RESULT_CODE = 'Введите код результата'
PLACEHOLDER_DESCRIPTION = 'Введите описание'

DIALOG_EXPORT_TITLE = 'Выберите/Создайте файл'
DIALOG_EXPORT_EXTENSION = '*.csv'
DIALOG_EXPORT_PATH_TO_DB = '/'

DIALOG_IMPORT_TITLE = 'Выберите файл'
DIALOG_IMPORT_EXTENSION = '*.csv'
DIALOG_IMPORT_PATH_TO_DB = '/'

DIALOG_VIEW_TITLE = 'Информация'
DIALOG_BUTTON_DELETE = 'Удалить'
DIALOG_BUTTON_CANCEL = 'Отмена'

DIALOG_VIEW_STYLE = 'width: 500px;'
DIALOG_DELETE_STYLE = 'width: 300px;'
DIALOG_MESSAGE_STYLE = 'font-size: 30px;'

DIALOG_INFORMATION_STYLE = 'font-size: 20px;'

TAB_TEST = '     Тест     '
TAB_HISTORY = 'История'
TAB_ANALYZER = 'Настройки'
