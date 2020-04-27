"""
案例描述：
新房里有一些物品，使用类来定义家和物品的关系，以及随着物品增加，所占面积的变化。

优化：
修改对象值的方法：
1. 通过对象名修改：
    Home.addItem = 
2. 通过方法间接修改：
    Home.addItem()

设置属性值和获取属性值都通过方法来获取
在一个方法里获取自己的属性不需要用方法，获取其他方法的属性，需要定义方法
"""

class Home:
    def __init__(self, newArea):
        self.area = newArea
        self.containItems = []

    def __str__(self):
        msg = "家里当前面积是：" + str(self.area)

        if len(self.containItems) > 0:
            msg += "\t"
            msg += "家里的物品有：" 

            for temp in self.containItems:
                #msg += temp.name + ","
                msg += temp.getName() + ","

            msg = msg[:-1]
        else:
            msg += "\t"
            msg += "家徒四壁" 
        return msg

    def addItem(self, item):
        #if self.area > item.area:
        needArea = item.getArea()
        if self.area > needArea:
            self.containItems.append(item)
            #self.area -= item.area
            self.area -= needArea

class Bed:
    def __init__(self, name, area):
        self.name = name
        self.area = area
    
    def __str__(self):
        return self.name + "的大小是：" + str(self.area)

    def getName(self):
        return self.name

    def getArea(self):
        return self.area

home = Home(120)
print(home)

bed = Bed('双人床', 4)
print(bed)

home.addItem(bed)
print(home)

bed2 = Bed('单人床', 2.6)
print(bed2)

home.addItem(bed2)
print(home)