#定义一个类
class Cat:
  #属性
  
  # 特殊方法，当对象创建后一定会调用的方法
  # 当创建完一个对象后，立马会自动调用
  def __init__(self, newColor, newWeight, newGender):
    # 方法里添加属性
    self.color = newColor
    self.weight = newWeight
    self.gender = newGender
    print('自动调用')

  #方法
  # 只要是个方法，就一定可以加入形参
  def eat(self,a,b):
    # print('eat')
    print(self.color, self.weight, 'eat a=%s,b=%d'%(a,b))

  def drink(self):
    print('drink')

  # 方法中获取值，直接给对象添加属性
  def printInfo(self):
    #print('我的猫是一只%s' % self.color, '的%s' % self.weight,'公斤重的%s' % self.gender, '猫', sep='')
    print('我的猫是一只', self.color, '的', self.weight,'公斤重的', self.gender, '猫。', sep='')
    # print(self.weight)
    # print(self.gender)
    # print(self.high)

# 创建一个猫对象
mao = Cat('灰色','5','公')
mao.eat('橘色',4)
#mao.drink()

mao.printInfo()

"""
# 给对象添加属性
mao.color = "橘"
mao.weight = 3
mao.gender = "f"

# 获取猫对象的数据
a = mao.color
print(a)
print(mao.gender)

# 注意：如果没有属性，那么还偏要访问这个属性，那么会产生一个异常
# print(mao.high)
"""

