# 第十章 输入输出

1. 输出

    print()
    将输出的值转为字符串：
    str(): 返回一个用户易读的表达式
    repr()：产生一个解释器易读的表达式，参数可以是任何对象

    ```python
    >>> s = 'hello world!'
    >>> s.title()
    'Hello World!'
    >>> str(s)
    'hello world!'
    >>> repr(s)
    "'hello world!'"
    >>> print(s)
    hello world!
    >>> list = ['asd','qqq','222']
    >>> repr(list)
    "['asd', 'qqq', '222']"
    >>> tuple = ('11','aa')
    >>> repr(tuple)
    "('11', 'aa')"
    >>> dict = {'a':22, 'c': 44}
    >>> repr(dict)
    "{'a': 22, 'c': 44}"
    ```

    ```python
    >>> for x in range(1,11):
    ...  print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
    ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
    10 100 1000
    ```

2. str.format()用法

    ```python
    >>> for x in range(1,11):
    ...  print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
    ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
    10 100 1000
    ```

3. 输入

    ```python
    >>> str = input("请输入姓名:")
    请输入姓名:dino
    >>> str
    'dino'
    ```

4. 从文件读取内容

```python
>>> str = open('ai.txt').readline()
>>> print(str)
人工智能并不是一个新的术语，它已经有几十年的历史了，大约从80年代初开始，

>>> str = open('ai.txt').readlines()
>>> print(str)
['人工智能并不是一个新的术语，它已经有几十年的历史了，大约从80年代初开始，\n', '计算机科学家们开始设计可以学习和模仿人类行为的算法。在算法方面，最重要的\n', '算法是神经网络，由于过拟合而不是很成功（模型太强大，但数据不足）。尽管如\n', '此，在一些更具体的任务中，使用数据来适应功能的想法已经取得了显着的成功，\n', '并且这也构成了当今机器学习的基础。在模仿方面，人工智能专注于图像识别，语\n', '音识别和自然语言处理。人工智能专家们花费了大量的时间来创建诸如边缘检测，\n', '颜色配置文件，N-gram，语法树等。不过，这些进步还不足以达到我们的需求。\n']

>>> for line in open('ai.txt'):
...  print(line, end='')
...
人工智能并不是一个新的术语，它已经有几十年的历史了，大约从80年代初开始，
计算机科学家们开始设计可以学习和模仿人类行为的算法。在算法方面，最重要的
算法是神经网络，由于过拟合而不是很成功（模型太强大，但数据不足）。尽管如
此，在一些更具体的任务中，使用数据来适应功能的想法已经取得了显着的成功，
并且这也构成了当今机器学习的基础。在模仿方面，人工智能专注于图像识别，语
音识别和自然语言处理。人工智能专家们花费了大量的时间来创建诸如边缘检测，
颜色配置文件，N-gram，语法树等。不过，这些进步还不足以达到我们的需求。
>>>
```

思考是不是在为自己工作，如果真的想成为企业家。要仔细思考！

independent thinking
creative drivens

如果你继续努力，一切都有可能。
once in your life, try something. work hard at something. try to change. nothing bad can happen. - jack ma
