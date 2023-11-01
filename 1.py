import random
list1 = []
list2 = []
for i in range(15):
    for j in range(3):
        list2.append(random.randint(1, 5))
    list1.append(list2)
    list2 = []
print(list1)