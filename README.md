# metaimage
Утилита для накладывания данных о сьёмки на фотографии.
Примеры: \
<img src="https://github.com/MagAcademy30/metaimage/raw/main/examples/IMG_2122.JPG" width="300">
<img src="https://github.com/MagAcademy30/metaimage/raw/main/examples/IMG_2149.JPG" width="300">
<img src="https://github.com/MagAcademy30/metaimage/raw/main/examples/_MG_4362.JPG" width="300">
## Возможности
 * Накладывание числа ISO, диафрагмы, выдержки и фокусного расстояния на фотографию
 * Настройка размера текста, сдвиг от краёв, пространство между строчками, его положение по углам и его прозрачность
## Как запустить
 * Windows: \
 Вам потребуется установить Python 3 с оффициального сайта, а после через командную строку выполнить команду:
 `pip install pillow exifread`
 После, можно запускать **run.bat** для запуска

 * Linux(Debian-based, Ubuntu):
 (Я не проверял)
 Вам потребуется установить Python 3 и менеджер пакетов pip а после установить библиотеки:
 ```
 sudo apt update 
 sudo apt python python3-pip -y
 pip install pillow exifread
 ```
 Уже после, можно запустить программу через команду:
 `python3 main.py`
## Настройка
Настройки хранятся в **config.txt**
Все настройки:
 * `font` - Путь к шрифту (По умолчанию это `font/CaviarDreams.ttf`)
 * `meta_opacity` - Прозрачность текста, задаётся от 0 до 255 (По умолчанию `255`)
 * `meta_size` - Размер шрифта (По умолчанию `250`)
 * `meta_position` - Угол расположения текста, пример: left-down, right-down, up-left (По умолчанию `left-down`)
 * `meta_offset` - Сдвиг от угла, `x,y` (По умолчанию `50,80`)
 * `meta_gap_beetwen_lines` - Пространство между линиями (По умолчанию `0`)
## To Do
 * Красивый удобный интерфейс
## Баги
На счёт багов, писать в issues или в телеграм - https://t.me/mg30_here
