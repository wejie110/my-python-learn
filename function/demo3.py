print(bool(0))
print(bool(1))


def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(fun(lst))
'''
函数的返回值
1.如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】return可以省略不写
2.如果函数的返回值是1个，直接返回类型
3.如果函数的返回值是多个，返回结果是元组

函数在定义时是否需要返回值，视情况而定
'''
