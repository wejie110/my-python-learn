name = 'ricky'  #name 称为全局变量
print(name)

def fun2(a, b):
    c = a+b     # a,b,c 称为局部变量
    print(c)
    print(name)


fun2(10,20)

def fun3():
    global age # 函数内部定义的变量，局部变量，局部变量用global声明 这个变量就变成了全局变量
    age = 22
    print(age)


fun3()
print(age)