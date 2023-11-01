# A. Не минимум на отрезке
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Задана последовательность целых чисел a1, a2, …, an. Задаются запросы: сказать любой элемент последовательности
# на отрезке от L до R включительно, не равный минимуму на этом отрезке.
#
# Формат ввода
# В первой строке содержатся два целых числа N, 1 ≤ N ≤ 100 и M, 1 ≤ M ≤ 1000 — длина последовательности и количество запросов соответственно.
#
# Во второй строке — сама последовательность, 0 ≤ ai ≤ 1000.
#
# Начиная с третьей строки перечисляются M запросов, состоящих из границ отрезка L и R, где L, R - индексы массива, нумеруются с нуля.
#
# Формат вывода
# На каждый запрос выведите в отдельной строке ответ — любой элемент на [L, R], кроме минимального. В случае, если такого элемента нет, выведите "NOT FOUND".
# Сообщение =  "NOT FOUND"
# индекс L минимум
# пройти по индексам L R
# если значение индекса больше L, то сообщение равно этому значению
# break
# если значение меньше L, тогда сообщение равно L
# break
# вывести сообщение

data1 = list(map(int, input().split()))
list_a = list(map(int, input().split()))
M = data1[1]
L = 0
while M > 0:
    message = "NOT FOUND"
    m = list(map(int, input().split()))
    L, R = m[0], m[1]
    for i in range(L, len(list_a)+R-len(list_a)+1):
        if list_a[i] > list_a[L]:
            message = str(list_a[i])
            break
        elif list_a[i] < list_a[L]:
            message = str(list_a[L])
            break
    M -=1
    print(message)


