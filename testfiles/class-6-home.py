"""
案例描述：
新房里有一些物品，使用类来定义家和物品的关系，以及随着物品增加，所占面积的变化。

"""

class Home:
    def __init__(self, newArea):
        self.area = newArea
        self.containItems = []

    def __str__(self):
        #return "新房面积是：" + str(self.area)
        msg = "家里当前面积是：" + str(self.area)

        if len(self.containItems) > 0:
            msg += "\t"
            msg += "家里的物品有：" 

            for temp in self.containItems:
                msg += temp.name + ","
            msg = msg[:-1]

            # msg += self.containItems[0].name
            # msg += ",".join(self.containItems)
        else:
            msg += "\t"
            msg += "家徒四壁" 
        return msg

    def addItem(self, item):
        if self.area > item.area:
            self.containItems.append(item)
            self.area -= item.area

class Bed:
    def __init__(self, name, area):
        self.name = name
        self.area = area
    
    def __str__(self):
        return self.name + "的大小是：" + str(self.area)


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