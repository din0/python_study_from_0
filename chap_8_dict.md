# 第八章 字典

1. 字典定义

    这里我们先回顾一下列表和元组：
    列表：list=[]
    元组：tuple=()
    列表的信息是可以修改的，但有的时候在设计过程中需要创建一些不可修改的元素。Python将不能修改的值称为不可变的，不可变的列表称为元组。元组中只包含一个元素时，需要再元素后加逗号。
    内置函数：将列表转换为元组：tuple(list)

    字典是一种可变容器模型，可存储任意类型对象，而且以组的形式进行数据存储。
    字典中包含两个关键字：键（key），值（value）

    dict = { key1: value1, key2: value2 }

    注意：由于目前我们爬取网站数据时，在JSON文件中，数据格式多为字典，所以一定要非常熟悉这种数据容器。

    例子：

    ```python
    >>> age = {'tom': 23, 'lisa': 22, 'john': 25}
    >>> age
    {'tom': 23, 'lisa': 22, 'john': 25}
    >>> age['lisa']
    22
    >>>
    ```

    ```python
    >>> student = {'name': 'tom', 'age': 23, 'gender': 'male'}
    >>> student['name']
    'tom'
    ```

2. 更新字典

    ```python
    >>> student
    {'name': 'tom', 'age': 23, 'gender': 'male'}
    >>> student['age']
    23
    >>> student['age'] = 24
    >>> student['age']
    24
    ```

3. 删除字典

    * 删除特定内容

    ```python
    >>> del student['gender']
    >>> student
    {'name': 'tom', 'age': 24}
    ```

    * 清空字典数据

    ```python
    >>> student.clear()
    >>> student
    {}
    ```

    * 删除字典

    ```python
    >>> del student
    >>> student
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'student' is not defined
    ```

4. 常用的函数和方法

    * 方法
    len(dict)：返回键的数量
    str(dict)：输出字符串格式

    * 函数
    dict.copy()：复制字典
    dict.items()：使用列表返回可遍历的元组数组
    dict.keys()：返回所有的键
    dict.values()：返回所有的值
    popitem()：返回并删除字典中的最后一对键和值
    dict.fromkeys(seq[,val])：创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
    dict.get(key, default=None)：返回指定键的值，如果值不在字典中返回default值
    dict.has_key(key)：如果键在字典dict里返回true，否则返回false
    dict.update(dict2)：把字典dict2的键/值对更新到dict里
    pop(key[,default])：删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
