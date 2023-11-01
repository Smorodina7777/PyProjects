# Даны две рациональные дроби: a/b и c/d. Сложите их и результат представьте в виде несократимой дроби m/n.
#
# Формат ввода
# Программа получает на вход 4 натуральных числа a, b, c, d, каждое из которых не больше 100.
#
# Формат вывода
# Программа должна вывести два натуральных числа m и n такие, что m/n=a/b+c/d и дробь m/n – несократима.
#
# Пример
# Ввод
# 1 2 1 2
# Вывод
# 1 1
#

list_nums = list(map(int, input().split()))
num_up = list_nums[0]*list_nums[3] + list_nums[2]*list_nums[1]
num_down = list_nums[1]*list_nums[3]
right_ind = min(num_down, num_up)//2
for i in range(2, right_ind +1):
    while num_up % i == 0 and num_down % i ==0:
        num_up //= i
        num_down //= i
        right_ind //=i
    if right_ind == i:
         break
print(num_up, num_down)