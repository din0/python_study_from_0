# 常用函数及方法


# 2. 请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
def cut(list):
    for i in range(0, len(list), 3):
        n_l = list[i:i+3]    # 列表切片的用法，查看第五章列表，此处b也是一个列表
        print(n_l, end=' ')

l = list(range(1,101))  # range()函数的用法，查看第五章列表
cut(l)

print("\n========================分隔符========================\n")

# 3. 请写出一段 Python 代码实现删除一个 list 里面的重复元素
lists = [1,2,3,4,5,6,7,2,3]
print(lists)
lists = list(set(lists))
print(lists)

print("\n========================分隔符========================\n")

# 6. 在不用其他变量的情况下，交换a、b变量的值
#6.1 python独有的用法
def exchange(a,b):
    a, b = b, a
    print(a,b)
exchange(2,3)

#6.2 通过简单的逻辑运算来实现
def exchange1(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(a,b)
exchange1(2,3)

#6.3 通过异或运算将a,b互换，二进制原理："1^1=0 1^0=1 0^0=0"
def exchange2(a,b):
    a = a^b
    b = a^b
    a = a^b
    print(a,b)
exchange2(2,3)

#6.4 使用变量实现
def exchange3(a,b):
    demo = a
    a = b
    b = demo
    print(a,b)
exchange3(2,3)

print("\n========================分隔符========================\n")

# 5. 写出一个函数,给定参数 n,生成含有 n 个元素值为 1~n 的数组,元素顺序随机,但值不重复
import random

def ran(n):
    r_list = list(range(1,n+1))
    r_lists = random.sample(r_list, n)
    print(r_lists)
ran(10)
'''
random模块：可以生成随机浮点数、整数、字符串，打乱数据。
函数：
1)random() 返回0<=n<1之间的随机实数n；
2)choice(seq) 从序列seq中返回随机的元素；
3)getrandbits(n) 以长整型形式返回n个随机位；
4)shuffle(seq[, random]) 原地指定seq序列；
5)sample(seq, n) 从序列seq中选择n个随机且独立的元素；
方法：
random.random()函数是这个模块中最常用的方法了，它会生成一个随机的浮点数，范围是在0.0~1.0之间。
random.uniform()正好弥补了上面函数的不足，它可以设定浮点数的范围，一个是上限，一个是下限。
random.randint()随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值，python random.randint。
random.choice()可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。
random.shuffle()如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。
random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。
'''
print("\n========================分隔符========================\n")

# 7. 如何在一个 function 里设置一个全局变量
name = 'dino'
def fun():
    global name
    name = 'tom'
    print(name)
fun()


# 8.输出？
def exlist(val, list=[]):
    list.append(val)
    return list

list_a = exlist(10)
print(list_a)
# list_b = exlist(123,['a','b','c'])
list_c = exlist(20)
print(list_c)
list_d = exlist('ccc')

# print(list_b)
print(exlist('ee'))