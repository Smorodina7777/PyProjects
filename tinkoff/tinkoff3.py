n = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
subList1 = []
subList2 = []
subList_djo = []
if list1 == list2:
    message = 'YES'
else:
    for i in range(len(list1)):
        if list1[i] ==list2[i] and len(subList1)>0:
            subList2.append(subList1)
            subList1 = []
        elif list1[i] !=list2[i]:
            subList1.append(list2[i])
            subList_djo.append(list1[i])
    if len(subList1)>0:
        subList2.append(subList1)
    if len(subList2) ==1 and len(subList2[0])>0 or (sorted(list1) == list2):
        if len(subList2[0]) ==1 and subList2[0]!= subList_djo:
            message = 'NO'
        elif sorted(subList2[0]) == subList2[0] == sorted(subList_djo):
             message = 'YES'
        else:
            message = 'NO'
    else:
        message = 'NO'
print(message)