def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


def fun1(*args):
    print(args)


def fun2(**kwargs):
    print(kwargs)


# 函数调用
fun(10, 20, 30)
lst = [11, 21, 31]
fun(*lst)  # 在函数调用时 将列表中的每个元素都转换为位置实参传入
fun1(*lst)
print('----------------------------')
fun(a=100, b=200, c=300)
dic = {'a': 101, 'b': 201, 'c': 301}
fun(**dic)
fun2(**dic)
