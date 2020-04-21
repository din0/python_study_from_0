# 第五章 列表 LIST

1. 定义列表

list=[]
names=['tom','jimmy','john']
names.append('dino')
names
['tom', 'jimmy', 'john', 'dino']

2. 列表中元素的访问和定义
name[1]='jim'
names
['tom', 'jim', 'john', 'dino']

3. 编辑列表
列表末尾添加：append()
列表开头插入：insert()

删除元素：del list[i]
pop()

>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12]
>>> nums.pop(10)
10
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

删除列表值：remove()

4. 列表排序：
sort(): 永久排序
sorted()：临时排序

  ```python
  >>> lans = ['python','java','c','php']
  >>> sorted(lans)
  ['c', 'java', 'php', 'python']
  >>> lans
  ['python', 'java', 'c', 'php']
  >>> lans.sort()
  >>> lans
  ['c', 'java', 'php', 'python']
  >>> lans.sort(reverse=True)
  >>> lans
  ['python', 'php', 'java', 'c']
  ```

反转列表：reverse()

  ```python
  >>> lans = ['python', 'php', 'java', 'c']
  >>> lans.reverse()
  >>> lans
  ['c', 'java', 'php', 'python']
  ```

列表长度：len()

  ```python
  >>> lans = ['python', 'php', 'java', 'c']
  >>> len(lans)
  4
  ```

列表中的函数：
列表中的方法：

5. 遍历列表

  ```python
  >>> lans = ['python', 'php', 'java', 'c']
  >>> for l in lans:
  ...  print(l)
  ...
  python
  php
  java
  c
  >>>
  ```

6. 创建整数列表，一般用在for循环中
range(start, stop[, step])

  ```python
  >>> for i in range(5):
  ...  print(i)
  ... 
  0
  1
  2
  3
  ```

7. 数字列表简单的计算

  ```python
  >>> nums = []
  >>> for num in range(0,11):
  ...  nums.append(num)
  ...
  >>> nums
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  >>> min(nums)
  0
  >>> max(nums)
  10
  >>> sum(nums)
  55
  >>>
  ```

8. 列表切片

```python
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> nums[0:3]
[0, 1, 2]
>>> nums[1:3]
[1, 2]
>>> nums[:3]
[0, 1, 2]
>>> nums[1:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> nums[-2:]
[9, 10]
>>> 
```

9. 遍历切片

  ```python
  >>> nums
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  >>> for i in nums[:4]:
  ...  print(i)
  ...
  0
  1
  2
  3
  >>>
  ```

10. 复制列表

  ```python
  >>> nums
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  >>> ten = nums[:]
  >>> ten
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ```

11. 元组
列表的信息是可以修改的，但有的时候在设计过程中需要创建一些不可修改的元素。Python将不能修改的值称为不可变的，不可变的列表称为元组。元组中只包含一个元素时，需要再元素后加逗号。

列表使用方括号表示，list = []
元组使用圆括号表示，tuple = ()
内置函数：
* 将列表转换为元组：tuple(list)

```python
>>> tuple=(12,23,'key')
>>> tuple
(12, 23, 'key')
>>> tuple[2]
'key'
>>> for i in tuple:
...  print(i)
...
12
23
key
>>>
```

12. 修改元组
```python
>>> menu=('stick','soup','fish','burger','crab')
>>> for i in menu:
...  print(i)
...
stick
soup
fish
burger
crab

#修改元组
>>> menu[3]
'burger'
>>> menu[3]='cheesecake'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> menu=('stick','soup','fish','cheesecake','crab')
>>> menu
('stick', 'soup', 'fish', 'cheesecake', 'crab')

#增加元组
>>> menu_add=('chicken','beef')
>>> menu=menu+menu_add
>>> menu
('stick', 'soup', 'fish', 'cheesecake', 'crab', 'chicken', 'beef')

#删除元组
>>> del menu
>>> menu
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'menu' is not defined
```




for i in range(len(names)):
  print(names[i])
  list.append(names[i])

list
['tom', 'jimmy', 'john', 'dino']



异常：
for语句后的冒号；
for循环内语句缩进






## 问题：
函数和方法的区别，如: sort(), sorted()

python 函数和方法，函数和方法两个概念经常有人搞混，python是解释性语言，也是面向对象的语言，那么调用函数和方法的方式就是最大的区别了，

## 函数：
1. 

abc = "abc"
print(abc)
最常见的函数是内置函数，比如print()就是，内置函数都已经设定好了，由名字和括号来进行调用，括号里面加入参数。

2. 
def quote():
    print("abc")
quote()
自定义函数，我们需要用def来进行函数的自定义，调用函数和内置函数的方法是一样的。

3. 
abc = lambda x, y: x * y
print(abc(2, 3))
匿名函数，这里需要用lambda作为关键字来使用，参数可以多个调用，不需要函数名。

4. 
def hey(n):
    if n==1:
        return 1
    return n * hey(n - 1)
print(hey(6))
递归函数，在函数里面调用函数，千万要避免死循环。

## 方法

1. 
list = [1, 2, 3, 4]
list.pop()
print(list)
pop()这里是list里面一个方法，方法不能单独使用，而是要配合对象来使用。

## 类中的函数和方法
1. 
class Animal():
    def barking(self):
        print("barking...")
tiger = Animal()
tiger.barking()
创建一个类，这里进行实例化，实例调用了方法，这里就不是函数了。

2. 
class Animal():
    def barking(self):
        print("barking...")
Animal.barking("Hey")
但是如果是这么执行就是调用函数，而不是方法了。

主要是看如何调用。


sorted()是内置函数，使用时 sorted(list)
而 srot()是方法，使用时 list.sort()，括号中为传递参数，reverse=True

### python中函数和方法的区别
首先摒弃错误认知:并不是类中的调用都叫方法
```
'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：579817333 
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
class Foo(object):

    def func(self,name):
        print('hello '+name)

#实例化
obj = Foo()

# 执行方式一:调用的func是方法
obj.func('zhangsan') #func 方法

# 执行方式二：调用的func是函数
Foo.func('self','lisi') # 函数
```

1.类对象调用func是方法，类调用func是函数，并且是自己传递参数！
2.函数要手动传self，方法不用传self

最大的区别是参数的传递参数，方法是自动传参self，函数是主动传参
那么以后我们就可以直接看参数是如何传递的来判断