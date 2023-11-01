set1 = set()
list2=[0, 0, 0]
str1 =''
for i in range(5, 10, 2):
    list2[0]=i
    for j in  range(0, 10):
        list2[1]=j
        for k in range(0, 10):
            if k==0 or not k % 3 == 0:
                list2[2] = k
            for c in list2:
                str1 = str1 + str(c)
            set1.add(str1)
            str1 = ''
list1 = list(set1)
list1.sort()
print(*list1)