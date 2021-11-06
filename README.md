# Лицей Академии Яндекса
## Проектная работа № 1 PyQT
#### Работу выполнила Сабельникова Влада Яновна школа 1560 Москва

### Постановка задачи
Написать приложение, которое реализует тест Люшера и Деллингер (два в одном),
с возможностью сохранения результатов анализа и накопления базы данных для 
дальнейшего использования.


### Принцип работы программы

Для запуска из корневой папки программы введите:

      $ python luscher.py

Или (только для Windows):

      $ luscher.exe
В появившемся окне есть три вкладки:
1. Тест
2. История
3. Настройки

Для того, что бы пройти тестирование нажмите кнопку "Старт".
После завершения тестирования вы сможете сохранить результат.

Если вы хотите просмотреть сохранённые результаты — перейдите во вкладку 
"История".

Если вы хотите изменить настройки, перейдите во вкладку "Настройки".


### Кому пригодится
1. Ученым, желающим накопить базу с результатами для своих 
исследований в области психологии.
2. HR-ам, для тестов при приеме на работу.
3. Людям, чья профессия связана с выдержкой и внимательностью
(военным, водителям, хирургам и т.д), для самопроверки.

### Используемые технологи
1. Стандартные виджеты PyQT, которые рассматривались в рамках курса.

    Такие как:
   * QHBoxLayout
   * QTableView
   * QGridLayout
   * QPushButton

       ...


2. Виджеты, которые не рассматривались в рамках курса.

    Такие как:
   * QStackedWidget
   * QDialog
   * QMessageBox
   * QTabWidget

       ...


3. Стандартные диалоги.

    Такие как:
   * QFileDialog


4. Формы.

    Такие как:
   * QLineEdit
   * QPlainTextEdit


5. Работа с изображениями. Создание картинок с помощью Pillow.


6. Работа с csv файлами.

    Конвертирование sqlite в csv и наоборот с помощью csv.writer()


7. Создание базы данных и нескольких таблиц.


8. Чтение, добавление, изменение, удаление в таблицах базы данных с помощью sqlite3


9. Создание пакетов, для удобного размещение файлов.


10. Возможность выявить коэффициент совпадения между двумя строками с помощью difflib


11. requirements.txt


12. exe файл