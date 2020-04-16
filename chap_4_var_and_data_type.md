# 第四章 变量和简单数据类型

1. 变量
    变量通常是定义用来存储计算结果或者表示特定值的简短易记的名字。
    1.1. python3的关键字（注意：不要使用关键字来自定义变量或者类名称。）

    ```python
   
    ```

    -|-|内置函数|-|-
    -|-|-|-|-
    abs() | delattr() | hash() | memoryview() | set()
    all() | dict() | help() | min() | setattr()
    any() | dir() | hex() | next() | slice()
    ascii() | divmod() | id() | object() | sorted()
    bin() | enumerate() | input() | oct() | staticmethod()
    bool() | eval() | int() | open() | str()
    breakpoint() | exec() | isinstance() | ord() | sum()
    bytearray() | filter() | issubclass() | pow() | super()
    bytes() | float() | iter() | print() | tuple()
    callable() | format() | len() | property() | type()
    chr() | frozenset() | list() | range() | vars()
    classmethod() | getattr() | locals() | repr() | zip()
    compile() | globals() | map() | reversed() | __import__()
    complex() | hasattr() | max() | round() | -

    1.2 Python的可执行文件的后缀为 .py，执行命令如下：

    ```python
    $ python3 test.py
    ```

    1.3 输出函数 Print()

    ```python
    >>> print("hello world!")
    hello world!
    ```

    1.4 定义变量

    ```python
    >>> msg = "hello world!"
    >>> print(msg)
    hello world!

    >>> name = "John"
    >>> name = "Tom"
    >>> print(name)
    ?
    ```

2. 字符串

    2.1 Python中的字符串，即使用单引号或者双引号括起来的内容。Python中对独立展示的字符串，单双引号可以互换使用，但若同时使用在一个对象上时，需要注意方法。

    ```python
    >>> question = "What's his name?"
    >>> answer = 'His name is "John"!'
    >>> print(question)
    >>> print(answer)
    What's his name?
    His name is "John"!
    ```

    2.2 常见文本处理内置函数

    ```python
    >>> hi = "hello world!"
    >>> print(hi.title())   #首字母大写
    Hello World！
    >>> print(hi.upper())   #全部大写
    HELLO WORLD!​
    >>> print(hi.lower())   #全部小写
    hello world!​
    ```

    2.3 字符串合并

    ```python
    >>> question = "What's his name?"
    >>> answer = "His name is"
    >>> name = "john"
    >>> print(question + " " + answer + " " + name.title() + "!")
    What's his name? His name is John!
    ```

    2.4 制表符和换行符

    ```python
    >>> print("John")
    John
    >>> print("\tJohn")
    	John
    >>> print("\nJohn")

    John
    >>> print("Programming Languages: \n\tPython\n\tJAVA\n\tPHP")
    Programming Languages:
        Python
        JAVA
        PHP
    ```

    2.5 删除空格

    ```python
    >>> name = "  John "    #前面空两格后面空一格
    >>> name
    '  John '
    >>> name.strip()    #删除所有空格
    'John'
    >>> name.lstrip()   #删除左侧空格
    'John '
    >>> name.rstrip()   #删除右侧空格
    '  John'
    ```

3. 数字
    3.1 整数 int

    ```python
    >>> 2+3
    5
    >>> 2-3
    -1
    >>> 2*3
    6
    >>> 2/3
    0.6666666666666666  #小数点后16位
    >>> (2+3)*4/2
    10
    ```

    3.2 浮点数（float），就是有小数点的数字，Python在做部分计算时给出的结果是不确定的，目前了解即可。

    ```python
    >>> 2/3
    0.6666666666666666
    >>> 0.2+0.3
    0.5
    >>> 0.2-0.3
    -0.09999999999999998
    >>> 0.3-0.2
    0.09999999999999998
    >>> 0.2*0.3
    0.06
    >>> 0.2/0.3
    0.6666666666666667
    ```

    3.3 str()函数

    ```python
    >>> age = 36
    >>> question = "How old are you?"
    >>> answer = "I am "
    >>> print(question + " " + answer + str(age) + ".")
    How old are you? I am 36.
    ```

    这里可以尝试一下不使用 str() 函数的输出结果。

4. 注释
    4.1 单行注释

    ```python
    # 这是我的第一个Python程序
    ```

    4.2 多行注释

    ```python
    """
    这是我的第一个Python程序。
    我一定会努力学习哒！
    """
    ```

5. 那些新手遇到的坑
