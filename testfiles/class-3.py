# 模板
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print('汪汪')
    
    def changeColor(self,newColor):
        self.color = newColor
        
    def printColor(self):
        print('旺财是一只%s' % self.color,'的狗子。')

    def printInfo(self):
        print(self.name, '是一只', self.color,'的狗子。', sep='')

def test(AAA):
    AAA.printColor()

# 创建对象
wangcai = Dog('旺财', '白色')
#wangcai.printColor()
wangcai.printInfo()

#wc.color = "白色"
#a = wc.color
xiaohei = Dog('小黑', '黑色')
#xiaohei.printColor()
xiaohei.printInfo()

test(wangcai)