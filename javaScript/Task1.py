# @param massivChisel: number[]
#   @param chislo: number[]
#   @return Array<Array<number>>
# */
# function sostavChisla(massivChisel, chislo) {
# 	// код писать только внутри данной функции
# 	return [[1, 2], [3]];
# }
# def sostavChisla(massivChisel, chislo):
#     massivChisel = sorted(massivChisel)
#     seq = []
#     chislo2 = 0
#     for i in massivChisel:
#         if chislo2<chislo:
#             chislo2 += i
#             if chislo2>chislo:
#
#             seq.append(i)
#     return
# chislo = 8
# massivChisel = [1, 2, 3, 4, 5, 6, 7, 8]





# def f(a, n, p):
#     if n:
#         for i in range(n + 1, 0, -1):
#             if i <= p:
#                 f(a + [i], n - i, i)
#     else:
#         print(*a, sep=' + ')
#
# n = int(input())
# f([], n, n)
def f2(n, m):
    a =[]
    p=n
    f(a, n, p, m)


def f(a, n, p, m):
    m=sorted(m)
    setlist = set(a)
    if sum(m)<n:
        print(*a, sep=' + ')
    elif n:
        for i in range(n + 1, 0, -1):
            if i <= p and len(a) == len(setlist) and set(a).issubset(m):
                f(a + [i], n - i, i, m)

    elif len(a) == len(setlist) and set(a).issubset(m):
        print(*a, sep=' + ')

n = 8
m= [8, 2, 3, 4, 6, 7, 1]
f2( n, m)



# def f(a,n1, n, p, m):
#
#     if sum(a) != n1:
#
#         for i in range(n-1, 0, -1):
#             if m[i] <= p:
#                 k = m[len(m)-1]-m[i]
#                 f(a + [m[i]],n1, k , i, m)
#     else:
#         print(*a, sep=' + ')
#
#
# n = 8
# m = [1, 2, 3, 4, 5, 6, 7, 8]
# f([],n, n, n, m)