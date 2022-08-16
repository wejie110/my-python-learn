def fun(a, b=10):  # b 是在函数的定义处，所以b是形参，而且进行了复制  所以b称为默认值形参
    print('a=', a)
    print('b=', b)


def fun2(*args):  # 个数可变的位置形参
    print(args)


def fun3(**kwargs):
    print(kwargs)


fun2(10, 20, 30, 40)
fun3(a=11, b=22, c=33, d=44, e=55)


def fun4(a, b, *, c, d):  # 从* 之后的参数，在函数调用时只能采用关键字参数传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


print('--------需求：c d 只能采用关键字实参传-------------')
# 调用fun4函数
# fun4(10, 20, 30, 40)
# fun4(a=11, b=22, c=33, d=44)
fun4(10, 20, c=30, d=40)

'''函数定义时的形参的顺序问题'''


def fun5(a, b, *, c, d, **kwargs):
    pass


def fun6(*args, **kwargs):
    pass


def fun7(a, b=10, *args, **kwargs):
    pass
