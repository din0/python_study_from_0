class Car:
  def __init__(self, newWheelNum, newColor):
    self.wheelNum = newWheelNum
    self.color = newColor

  def move(self):
    print('destination: China')

  def printInfo(self):
    print('我的车是一辆',self.color,'的',self.wheelNum,'轮汽车。', sep='')

BMW = Car(4, '蓝色')

BMW.printInfo()

#print('color is:%s'%BMW.color)
#print('wheel number is:%d'%BMW.wheelNum)

