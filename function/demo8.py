"""递归函数"""


def fac(a):
    if a == 1:
        return 1
    else:
        return a * fac(a - 1)


print(fac(6))


'''斐波那契数列'''


def flb(n):
    if n == 1 :
        return 1
    elif n == 2:
        return 1
    else:
        return flb(n-2)+flb(n-1)


for i in range(1, 7):
    print(flb(i))


