# 第十一章 类

1. 面向对象基本概念：

    面向过程：根据业务逻辑考虑到每一步流程去编写
    面向对象：只面对结果，不需要考虑过程。

    类和对象
    类是模型
    对象是实体，最终成果
    举例:月饼和模具

    区分类和对象
    对象是具体的一个物品

    区分类和对象：
    猫
    橘猫
    我的橘猫

    叼着热狗的狗

    类是由函数和对象组成的，即：方法和属性，
    类名：名称  狗
    属性：一组数据，自身属性  什么狗
    方法：允许操作的方法，赋予的动作和行为   叫，跳，咬

    现实中是先有对象才有类

    类的抽象：有共同属性和行为的对象都可以抽想出一个类

2. 类的定义

    类和函数的区别：类是面向对象中实现信息封装的基础；函数是指一段执行程序用于实现一个功能，在面向对象中称为方法。类中包括：方法/函数，属性，构造函数等。

    Python类的定义：
    * 使用class关键字定义一个类，并且类名首字母要大写；
    * 当需要创建的类型不能用简单类型表示时就要创建类；
    * 类把需要的变量和函数组合在一起，称之为“封装”

    对象的创建：
    创建对象的过程称为实例化，当一个对象被创建后，包含三个特性：句柄（名字，用来区分及调用）、属性（类中定义的内部变量）、方法（类里面的函数）；

    创建类时，做一个判断：

    ```python
    if __name__ == "__main__":
        myClass1 = MyClass()
    ```

    封装、继承、多态

    ```python
    class ClassName:
        <statement-1>
        ...
        <statement-N>
    ```

    类名规则：大驼峰

    给一个对象添加属性方法：
    对象名.新的属性名 = 值

    获取这个对象的属性，2种方法：
        1. 对象.属性
        2. 定义一个方法，这个方法中，使用self.属性

    ```python
    #定义一个类
    class Cat:
        #属性:给对象添加属性

        #方法
        def eat(self):
            print('eat')
        def drink(self):
            print('drink')

        #def printInfo(self):

    # 创建一个猫对象
    huamao = Cat()
    huamao.eat()
    huamao.drink()

    # 给对象添加属性
    huamao.color = "colored"
    huamao.weight = 3
    ```

3. __init__() 方法

    1. 创建完之后，立即自动调用的方法.
    2. 不需要开发者调用，即 对象名.__init__()
    3. 这个方法一般会完成一些默认的事件，比如添加一些初始化的自有属性
    4. 写法
        class className:
            def __init__(self, new_a, new_b):
                self.a = new_a  #添加新属性
                self.b = new_b

    注意：
    self.a 是添加一个新的属性，new_a是形参，局部变量，在函数/方法内部使用。
    new_a, new_b 是方法内的局部变量，不是对象的属性；若要在init方法中添加属性。
    需要使用 self.属性名 = 值，
    self.a = new_a 表示的是给对象添加一个属性，属性名为a，属性的值为局部变量new_a中的值。

    其他：
    print()语法
    print()中使用逗号分隔语句和变量时，会出现多余的空格；此时若想去掉这些空格，可以在后面加上sep=''，如下：
    print(*objects, sep=' ', end='\n', file=sys.stdout)

    参数：
    * objects – 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
    * sep – 用来间隔多个对象，默认值是一个空格。
    * end – 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
    * file – 要写入的文件对象。

    示例：

    ```python
    >>> a = 'Hello'
    >>> b = 'World'
    >>> print(a,b)      # 直接打印，分隔符默认有一个空格
    Hello World
    >>> print(a,b,sep='') # 分隔符 设置为空
    HelloWorld
    >>> print(a,b,sep=".")  # 分隔符设置为.
    Hello.World
    ```

    ```python
    >>> print('我的猫是一只%s' % self.color, '的%s' % self.weight,'公斤重的%s' % self.gender, '猫', sep='')
    我的猫是一只灰色 的5 公斤重的公 猫
    >>>print('我的猫是一只', self.color, '的', self.weight,'公斤重的', self.gender, '猫。', sep='')
    我的猫是一只灰色的5公斤重的公猫
    ```

    ```python
    >>> for i in range(6):
    ...  for j in range(i):
    ...   print('*',end='')
    ...  print()
    ...
    *
    **
    ***
    ****
    *****
    ```

4. __self__() 方法

    ```python
    # 模板
    class Dog:
        def __init__(self, name, color):
            self.name = name
            self.color = color

        def printInfo(self):
            print(self.name, '是一只', self.color,'的狗子。', sep='')

    def test(AAA):
        AAA.printColor()

    # 创建对象
    wangcai = Dog('旺财', '白色')
    wangcai.printInfo()

    xiaohei = Dog('小黑', '黑色')
    xiaohei.printInfo()

    test(wangcai)
    ```

    总结：
    先看到对象，然后描述并抽象出类。
    创建类，然后在对象中增加属性。
    如果想要调用一个对象中的一个方法，先根据对象找到存储的地方，然后去对应的类中找到存储的函数。

    魔法方法

    具有特殊功能的方法就叫”魔法方法“：如__init__,__str__

5. __str__() 方法

    用来将内存中对象存储的位置返回为存储的信息。

    ```python
    def __str__(self):
            return '当前对象的颜色为：' + self.color
    print(wangcai) # 打印内存地址
    print(xiaohei)
    <__main__.Dog object at 0x1021b6810>
    <__main__.Dog object at 0x1021b6a50>
    当前对象的颜色为：白色
    当前对象的颜色为：黑色
    ```

6. 应用实例：

    实例描述：
    BBQ：
    cookedLevel:    cookedString:       condiments:
    <3              '生的'               调料 = []
    <5              '半生不熟'
    <8              '熟的'
    >8              '糊了'

    ```python
    class BBQ:
        # 初始化对象
        def __init__(self):
            self.cookedLevel = 0
            self.cookedString = '生的'
            self.condiments = []

        def __str__(self):
            #return '烤了' + str(self.cookedLevel) + '分钟,肉' + self.cookedString + '，调料有：' + str(self.condiments) + '。'
            msg = '烤了' + str(self.cookedLevel)
            msg += '分钟,肉' + self.cookedString
            if len(self.condiments)>0:
                msg += '，调料有：' #+ str(self.condiments) + '。'

                for i in self.condiments:
                    msg += i + '，'

                msg = msg[:-1] + '。'
                # msg = msg.strip('，')
            else:
                msg += '，还没有添加调料。'
            return msg

        def cook(self, times):
            self.cookedLevel += times
            if self.cookedLevel < 3:
                self.cookedString = '生的'
            elif self.cookedLevel < 5:
                self.cookedString = '半生不熟'
            elif self.cookedLevel < 8:
                self.cookedString = '熟了'
            else:
                self.cookedString = '烤糊了'

        def addCondiments(self, condiment):
            self.condiments.append(condiment)

    bbq = BBQ()
    print(bbq)

    bbq.cook(1)
    print(bbq)
    bbq.addCondiments('芥末')
    print(bbq)
    bbq.cook(2)
    print(bbq)
    bbq.cook(2)
    bbq.addCondiments('紫菜')
    print(bbq)
    bbq.cook(3)
    bbq.addCondiments('孜然')
    print(bbq)
    bbq.cook(3)
    print(bbq)
    ```

    Outputs:

    ```python
    烤了0分钟,肉生的，还没有添加调料。
    烤了1分钟,肉生的，还没有添加调料。
    烤了1分钟,肉生的，调料有：芥末。
    烤了3分钟,肉半生不熟，调料有：芥末。
    烤了5分钟,肉熟了，调料有：芥末，紫菜。
    烤了8分钟,肉烤糊了，调料有：芥末，紫菜，孜然。
    烤了11分钟,肉烤糊了，调料有：芥末，紫菜，孜然。
    ```
