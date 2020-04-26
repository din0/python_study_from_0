class MyClass:
    i=12345
    def f(self):    # self表示类的实例
        return 'hello world!'
    
    def fib(self, n):    # 定义到 n 的斐波那契数列
        a, b = 0, 1
        while b < n:
            print(b, end=' ')
            a, b = b, a+b
        # print()

# 实例化类
x = MyClass()

print('属性:', x.i)
print('方法:', x.f())
print('fib:',x.fib(100))