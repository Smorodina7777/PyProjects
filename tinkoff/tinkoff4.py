list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

def f2(n, m):
    a =[]
    p=n
    f(a, n, p, m)


def f(a, n, p, m):
    m=sorted(m)
    list = a
    if sum(m)<n:
        print(len(a))
        print(*a, sep=' ')

    elif n:
        for i in range(n + 1, 0, -1):
            if i <= p and len(a) == len(list) and a.issubset(m):
                f(a + [i], n - i, i, m)

    elif len(a) == len(list) and a.issubset(m):
        print(len(a))
        print(*a, sep=' ')

n = list1[0]
m= list2
f2( n, m)

