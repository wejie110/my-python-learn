print("hello world")


def calc(a, b):   # a, b 形式参数  形参  形参的位置是函数的定义处
    c = a + b
    return c


result = calc(10, 20)   # 10，20实际参数的值    位置实际参数  简称 位置实参   实参的位置是函数的调用处
print(result)

res = calc(b=10, a=30)  # =左侧变量的名称为  关键字实际参数  简称关键字实参
print(res)






