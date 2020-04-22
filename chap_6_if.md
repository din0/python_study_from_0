# 第六章 条件语句 if...

1. 简单示例
if 条件：
  执行语句

例如：

```python
age=20
if a<18:
  print("你还是个未成年的小盆友！")
```

在上面这个例子里是不会有返回内容的，为什么？
因为age没有满足a<18这个条件，请试着把age改成17试一下。

2. if-else
if 条件1:
  执行语句1
else:
  执行语句2

例如：

```python
>>> age=20
>>> if age < 18:
...  print('你还是个小盆友!')
... else:
...  print('你成年了哦!')
...
你成年了哦!
```

3. 更加复杂的条件语句 if-elif-else

if 条件1:
  执行语句1
elif 条件2:
  执行语句2
else:
  执行语句3

例子：

```python
>>> age=20
>>> if age < 18:
...  print('你还是个小盆友!')
... elif age < 60:
...  print('你已经是个成年人了,要对自己的行为负责!')
... else:
...  print('干了一辈子,终于退休啦!')
...
你已经是个成年人了,要对自己的行为负责!
```

4. 查询列表，当满足一个条件执行相应语句后，将会跳过剩下的语句。

```python
>>> names = ['tom','john','lisa','jan']
>>> if 'jim' in names:
...  print('jim is here')
... elif 'tom' in names:
...  print('tom is here')
... else:
...  print('not here')
...
tom is here
```
