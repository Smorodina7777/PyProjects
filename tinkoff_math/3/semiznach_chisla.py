list1 =[]
str1 = ''
for i in range(1, 10):
    for z in range(i+1, 10):
        for x in range(z+1, 10):
            for c in range(x+1, 10):
                for v in range(c+1, 10):
                    for b in range(v+1, 10):
                        for n in range(b+1, 10):
                            if i*z*x*c == c+v+b+n:
                                print(i*z*x*c)
                                str1 = str1+ str(i)+ str(z) + str(x) + str(c) + str(v) + str(b) + str(n)
                                list1.append(str1)
                                str1 = ''
print(*list1)