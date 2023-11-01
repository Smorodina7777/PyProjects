# D. Анаграмма?
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Задано две строки, нужно проверить, является ли одна анаграммой другой. Анаграммой называется строка, полученная из другой перестановкой букв.
#
# Формат ввода
# Строки состоят из строчных латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.
#
# Формат вывода
# Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.
#
# Пример 1
# Ввод	Вывод
# dusty
# study
# YES
#



def add_char_to_dict(str):
    char_dict = {}
    for char in str:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict


str1 = input()
str2 = input()
char_dict1 = add_char_to_dict(str1)
char_dict2 = add_char_to_dict(str2)
if char_dict2 ==char_dict1:
    print('YES')
else:
    print('NO')
