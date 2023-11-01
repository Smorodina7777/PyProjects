list1 = [i+1 for i in range(1000)]
list2 = list1
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

list_sums = []

for i in list1:
    sum_i = sum_of_digits(i)
    list_sums.append(sum_i)

list_sums2 = list_sums

for i in range(1, 1000):
    for j in range(1000):
        if list_sums[i]<list_sums[j]:
            list_sums[i], list_sums[j] = list_sums[j], list_sums[i]
            list1[i], list1[j] = list1[j], list1[i]
for i in range(1, 1000):
    for j in range(1000):
        if list_sums[i]==list_sums[j] and list1[i] < list1[j]:
            list_sums[i], list_sums[j] = list_sums[j], list_sums[i]
            list1[i], list1[j] = list1[j], list1[i]
print(list_sums)
print(list1)
print(list1.index(996))