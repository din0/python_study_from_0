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

    def __str__(self):
        return '当前对象的颜色为：' + self.color

def test(AAA):
    AAA.printColor()

# 创建对象
wangcai = Dog('旺财', '白色')
#wangcai.printColor()
#wangcai.printInfo()

#wc.color = "白色"
#a = wc.color
xiaohei = Dog('小黑', '黑色')
#xiaohei.printColor()
#xiaohei.printInfo()

# test(wangcai)

print(wangcai) # 打印内存地址
print(xiaohei)
print(id(wangcai)) # 打印存储位置
print(id(xiaohei))