# 第九章 定义函数

1. 函数是一段编辑好的可以复用的代码块。前面我们用过一些python的内建函数。这里我们讲讲解如何自定义函数。

    ```python
    def 函数名(参数):
    函数内容
    return [返回表达式]
    ```

    函数定义：

    ```python
    >>> def func():
    ...  print('hello world!')
    ...
    >>> func()
    hello world!
    ```

    ```python
    >>> def func(str):
    ...   print(str)
    ...   return
    ...
    ```

    函数调用：

    ```python
    >>> func('function test!')
    function test!
    ```

2. 参数传递

    实参：调用函数时传递给函数的信息，如上方调用func()函数时，在括号里填写的：'function test!'；
    形参：函数完成其工作所需的信息，如上方定义函数func()时，括号里填写的：str；

    例子：我们定义一个字典student，使用函数stu(name, age)向字典中插入键和值，也叫位置实参

    ```python
    >>> student={}
    >>> student
    {}
    >>> def stu(name, age):
    ...  student['name']=name
    ...  student['age']=age
    ...
    >>> stu('tom', 23)
    >>> student
    {'name': 'tom', 'age': 23}
    ```

    例子：传入可变列表

    ```python
    >>> listA = [1,2,3]
    >>> listB = [4,5,6]
    >>> def list_append(a, b):
    ...  a.append(b)
    ...  print(a)
    ...
    >>> list_append(listA,listB)
    [1, 2, 3, [4, 5, 6]]
    ```

    ```python
    >>> def pet(type, name):
    ...  print('我有一只', type, '.')
    ...  print('我的',type, '的名字是', name)
    ...
    >>> pet('猫', '皮蛋')
    我有一只 猫 .
    我的 猫 的名字是 皮蛋
    ```

    默认值，在定义函数时，给某个形参设定默认值。调用函数时若没有给该形参设定值，则使用默认值。

    ```python
    >>> def pet(name, type='cat'):
    ...  print("my ", type, "'s name is ", name)
    ...
    >>> pet('kiko')
    my  cat 's name is  kiko
    >>> pet('kiko', 'dog')
    my  dog 's name is  kiko
    ```

    注意：有默认值的形参必须在后面，否则会报错。大家可以尝试下设定两个默认值的情况。

3. 返回值，可选实参

    ```python
    >>> def name(first_name, middle_name, last_name):
    ...  full_name = first_name + ' ' + middle_name + ' ' + last_name
    ...  return full_name.title()
    ...
    >>> name('tommy', 'lee', 'johns')
    'Tommy Lee Johns'
    ```

    但是不是所有人都有middle_name，那么如果没有middle_name的时候这个函数就会出现问题。

    ```python
    >>> name('tom', 'cruise')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: name() missing 1 required positional argument: 'last_name'
    >>> name('tom','', 'cruise')
    'Tom  Cruise'
    ```

    即使将middle_name空着，也会多出一个空格，所以我们需要一个条件语句来进行优化：

    ```python
    >>> def name(first_name, last_name, middle_name=''):
    ...  if middle_name:
    ...   full_name = first_name + ' ' + middle_name + ' ' + last_name
    ...  else:
    ...   full_name = first_name + ' ' + last_name
    ...  return full_name.title()
    ...
    >>> name('tommy', 'lee', 'jones')
    'Tommy Jones Lee'
    >>> name('tommy', 'jones', 'lee')
    'Tommy Lee Jones'
    >>> name('tom', 'cruise')
    'Tom Cruise'
    ```

    练习：

    ```python
    >>> cities=['xian','chengdu','beijing']
    >>> cities.append('tokyo')
    >>> cities
    ['xian', 'chengdu', 'beijing', 'tokyo']
    >>> countries=['china','japan']
    >>> city_country(cities[1],countries[0])
    Chengdu   China
    >>> city_country(cities[3],countries[1])
    Tokyo   Japan
    ```

    ```python
    >>> def make_album(album_name, singer):
    ...  album={'album_name:': album_name, 'singer:': singer}
    ...  return album
    ...
    >>> make_album('Parked Car Conv', 'Kaash Paige')
    {'album_name:': 'Parked Car Conv', 'singer:': 'Kaash Paige'}
    ```

    ```python
    >>> def make_album(album_name, singer, songs_no=''):
    ...  if songs_no:
    ...   album={'album_name:': album_name, 'singer:': singer, 'songs_no:': songs_no}
    ...   return album
    ...  else:
    ...   album={'album_name:': album_name, 'singer:': singer}
    ...   return album
    ...
    >>> make_album('Parked Car Conv', 'Kaash Paige', 8)
    {'album_name:': 'Parked Car Conv', 'singer:': 'Kaash Paige', 'songs_no:': 8}
    >>> make_album('six feet under', 'Billie Eilish')
    {'album_name:': 'six feet under', 'singer:': 'Billie Eilish'}
    ```

4. 传递列表

    遍历列表并输出列表元素：

    ```python
    >>> def hello(names):
    ...  for i in names:
    ...   msg = 'hello,' + i + '!'
    ...   print(msg)
    ...
    >>> hello(names)
    hello,tom!
    hello,lisa!
    hello,jim!
    ```

    列表传递：

    不用函数：

    ```python
    >>> warehouse = ['apple','orange','banana']
    >>> shop = []
    >>> while warehouse:
    ...  truck = warehouse.pop()
    ...  print(truck)
    ...  shop.append(truck)
    ...
    banana
    orange
    apple
    >>> shop
    ['banana', 'orange', 'apple']
    >>> warehouse
    []
    ```

    使用函数：

    ```python
    >>> def transport(warehouse, shop):
    ...  while warehouse:
    ...   truck = warehouse.pop()
    ...   print(truck)
    ...   shop.append(truck)
    ...
    >>> warehouse = ['apple','orange','banana']
    >>> shop = []
    >>> transport(warehouse, shop)
    banana
    orange
    apple
    >>> shop
    ['banana', 'orange', 'apple']
    >>> warehouse
    []
    ```

    传递列表后，保存原有列表：使用切片来创建原有列表的副本 list[:]

    ```python
    >>> transport(warehouse[:], shop)
    banana
    orange
    apple
    >>> warehouse
    ['apple', 'orange', 'banana']
    >>> shop
    ['banana', 'orange', 'apple']
    ```

    练习：
    伟大的魔术师：在新建列表中魔术师名字前面都加上’the great‘

    ```python
    >>> def make_great(magicians):
    ...  while magicians:
    ...   magician = magicians.pop()
    ...   great_magician = 'The Great ' + magician.title()
    ...   great_magicians.append(great_magician)
    ...  print(great_magicians)
    ...
    >>> magicians = ['criss angel','david blaine', 'david copperfield']
    >>> great_magicians = []
    >>> make_great(magicians[:])
    ['The Great David Copperfield', 'The Great David Blaine', 'The Great Criss Angel']
    ```

5. 不定数量实参

    不定长参数，使用 *，以元组的形式导入，存放未命名的变量参数。

    ```python
    >>> def infi(*tuple):
    ...  print(tuple)
    ...
    >>> infi('a','b','c')
    ('a', 'b', 'c')
    ```

    任意数量关键字实参，使用 **，以字典形式导入：

    ```python
    >>> def profile(first, last, **info):
    ...  prof = {}
    ...  prof['first_name'] = first
    ...  prof['last_name'] = last
    ...  for k, v in info.items():
    ...   prof[k] = v
    ...  return prof
    ...
    >>> profile('tom', 'cruise', location='USA', gender='male')
    {'first_name': 'tom', 'last_name': 'cruise', 'location': 'USA', 'gender': 'male'}
    ```

6. 导入外部函数模块: import语句

    新建 func.py 文件

    ```python
    def transport(warehouse, shop):
      while warehouse:
        truck = warehouse.pop()
        print(truck)
        shop.append(truck)
      print(shop)

    def hello(names):
      for i in names:
        msg = 'hello,' + i + '!'
        print(msg)
    ```

    test.py 执行文件

    ```python
    import func

    names = ['jim','tom','lisa']
    func.hello(names)

    warehouse = ['apple','orange','banana']
    shop = []
    func.transport(warehouse, shop)
    ```

    运行程序：

    ```python
    $ python3 test.py
    hello,dino!
    hello,tom!
    hello,lisa!
    banana
    orange
    apple
    ['banana', 'orange', 'apple']
    ```

7. 导入模块中特定的函数：from...import...
    test.py 执行文件

    ```python
    from func import hello, transport

    names = ['jim','tom','lisa']
    hello(names)

    warehouse = ['apple','orange','banana']
    shop = []
    transport(warehouse, shop)
    ```

8. 自定义函数名，模块名

    ```python
    from func import transport as trans

    trans()
    ```

    ```python
    import func as fn

    fn.hello(names)
    ```

9. 导入模块中所有函数

    ```python
    from func import *

    trans()
    ```

10. 总结：
    关于模块和函数的用法，平常我们会创建一个 models.py 文件用来写入自定义函数。当我们需要调用模块中所有函数的时候就可以使用：import models；需要调用模块中具体的函数时使用：from models import function；若需要调用模块中所有函数则使用：from models import * 。在我们使用Django来开发Web应用的时候，自定义函数都会写在应用目录下的models.py中以便于调用。

11. 深入模块

    __name__属性的使用
    当一个模块被引用时，如果想在引用时某一程序不执行，可以用__name__来使该程序块仅在该模块文件运行时执行：

    ```python
    if __name__ == '__main__':
      print('该模块运行时才执行')
    else:
      print('该模块文件被调用时执行')
    ```

    dir()函数：
    找到模块内定义的所有名称。

    ```python
    >>> import fibo
    >>> dir(fibo)
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
    ```

12. 包的用法
    注意当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。

    import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，抛出一个 :exc:ImportError 异常。

    反之，如果使用形如 import item.subitem.subsubitem 这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。
    