list1 = list(map(int, input().split()))
n = list1[0]
s = list1[1]
price = list(map(int, input().split()))
max =0
for cost in price:
    if max< cost and s>=cost:
        max = cost
print(max)