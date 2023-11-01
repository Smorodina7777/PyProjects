def find_max_carrot(max_carrot, sum_carrot):
    if sum_carrot > max_carrot:
        max_carrot = sum_carrot
    return max_carrot


num = list(map(int, input().split()))
N, M = num[0], num[1]
area = []
while N > 0:
    row = list(map(int, input().split()))
    area.append(row)
    N -= 1
max_carrot = 0
sum_carrot = sum(area[0])
max_carrot = find_max_carrot(max_carrot, sum_carrot)

sum_carrot = sum(area[len(area) - 1])
max_carrot = find_max_carrot(max_carrot, sum_carrot)

sum_carrot_left = 0
sum_carrot_right = 0
for row in area:
    sum_carrot_left += row[0]
    sum_carrot_right += row[M - 1]
max_carrot = find_max_carrot(max_carrot, sum_carrot_right)
max_carrot = find_max_carrot(max_carrot, sum_carrot_left)
print(max_carrot)
