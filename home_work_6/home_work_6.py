# Задание: подсчитайте количество уникальных слов в текстовом файле и запишите их в другой файл в алфавитном порядке.
#
# 1. Создайте в текстовом редакторе текстовый файл по имени “data.txt” и запишите в него любой произвольный текст.
# 2. Создайте функцию read_file. Функция должна принимать имя файла, прочитать его и вернуть список уникальных слов из этого файла в нижнем регистре.
# Создайте функцию save_file. Функция должна принимать имя файла для записи и список уникальных слов. В функции подсчитайте количество уникальных
# слов и запишите его в файл вместе со всеми словами отсортированными в алфавитном порядке.
# 3. Вынесите функции в отдельный файл, который нужно будет подключать с помощью import.
from my_file import read_file, save_file

my_list = read_file('data.txt')
save_file('data_out.txt', my_list)