n = int(input())
list_a = list(map(int, input().split()))
level_list = []
for i in range(len(list_a)):
    sum_level = 0
    for j in range(len(list_a)):
        level = abs(list_a[j] - list_a[i])
        sum_level += level
    level_list.append(sum_level)
print(*level_list)
