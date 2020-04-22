# 第七章 循环语句

1. for循环（也叫 for in）
    重复执行语句，直至判断条件为False

    for 变量 in 序列:
    执行语句

    例子：
    我们首先来复习一下之前讲过的range()

    ```python
    >>> num = list(range(1,5))
    >>> num
    [1, 2, 3, 4]
    #接下来我们用for in 让它打印四次
    >>> for i in range(1,5):
    ...  print(i)
    ...
    1
    2
    3
    4
    ```

    另一种方法

    ```python
    >>> for i in num:
    ...  print(i)
    ...
    1
    2
    3
    4
    ```

    打印字母：

    ```python
    >>> for letter in 'Python':
    ...  print(letter)
    ... 
    P
    y
    t
    h
    o
    n
    ```

    打印列表：

    ```python
    >>> names = ['tom','lisa','john','nick']
    >>> for i in names:
    ...  print(i)
    ...
    tom
    lisa
    john
    nick
    ```

    更加复杂的遍历用法：

    ```python
    >>> names = ['tom','lisa','john','nick']
    >>> for i in range(len(names)):     #len(names) 返回列表长度
    ...  print(names[i])
    ...
    tom
    lisa
    john
    nick
    ```

2. while循环
    在满足循环条件的前提下重复执行循环体，否则退出循环体
    while 判断条件：
    执行语句

    ```python
    >>> i = 1
    >>> while i<10:
    ...  print(i)
    ...  i+=1
    ...
    1
    2
    3
    4
    5
    6
    7
    8
    9
    ```

    注意：判断条件有两个结果，分别为：True和False，所以，若判断条件为True，且没有终止条件时，while循环会一直执行下去形成无限循环。
    如以上例子去掉i+=1，因为i=1满足i<10的条件，所以会持续执行变成无限循环：

    ```python
    >>> i = 1
    >>> while i<10:
    ...  print(i)
    ...
    1
    1
    1
    1
    1
    1
    ...
    ```

    注意：若出现无限循环，我们可以使用键盘组合键：Ctl+C来中断循环。

    continue和break：
    为了给while循环增加中止条件，我们可以用continue来跳过此次循环，用break来退出循环。

    例子：continue

    ```python
    >>> i = 1
    >>> while i<10:
    ...  i+=1
    ...  if i%2 != 0:    #若余数不为0，则为非双数，继续执行循环
    ...   continue
    ...  print(i)
    ...
    2
    4
    6
    8
    10
    ```

    例子：break

    ```python
    >>> i = 1
    >>> while 1:
    ...  print(i)
    ...  i+=1       #i=i+1
    ...  if i>10:   #若i大于10，则中断循环并跳出
    ...   break
    ...
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    ```

    循环使用else条件中止：

    ```python
    >>> i=1
    >>> while i < 10:
    ...  print(i, "小于10")
    ...  i+=2
    ... else:
    ...  print(i, "不小于10")
    ...
    1 小于10
    3 小于10
    5 小于10
    7 小于10
    9 小于10
    11 不小于10
    >>>
    ```

3. 循环嵌套
    for循环和while循环，以及if...else...条件语句可以嵌套使用

    ```python
    >>> i = 2
    >>> while(i < 10):
    ...    j = 2
    ...    while(j <= (i/j)):
    ...       if not(i%j): break
    ...       j = j + 1
    ...    if (j > i/j) : print(i, " 是素数")
    ...    i = i + 1
    ...
    2  是素数
    3  是素数
    5  是素数
    7  是素数
    ```

4. 使用循环处理列表

    * 移动元素

    ```python
    >>> listA = ['tom','lisa','john']
    >>> listB = []
    >>> while listA:
    ...  i = listA.pop()
    ...  listB.append(i)
    ...
    >>> listB
    ['john', 'lisa', 'tom']
    >>> listA
    []
    ```

    * 删除元素

    ```python
    >>> listB
    ['john', 'lisa', 'tom']
    >>> while 'tom' in listB:
    ...  listB.remove('tom')
    ...
    >>> listB
    ['john', 'lisa']
    ```
