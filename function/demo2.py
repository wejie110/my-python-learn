def fun(arg1, arg2):
    print('arg0=', arg1)
    print('arg1', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)


n1 = 11
n2 = [22, 33, 44]
print(n1)
print(n2)
print('-------------------')
fun(n1, n2)   # arg1 ,arg2 是函数定义处的形参，n1,n2是函数调用处的实参，总结：实参名称和形参名称可以不一致
print(n1)
print(n2)

'''在函数的调用中，进行参数的传递 
若是不可变对象，在函数体内的修改不会影响实参的值 arg1
若是可变对象，在函数体内的修改会影响到实参的值    arg2
'''