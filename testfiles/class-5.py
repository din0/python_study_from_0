"""
烤肉BBQ
cookedLevel：   0-3分钟 生的
                3-5 半生不熟
                5-8 分钟熟了
                >8分钟 糊了 

cookedString：  生的
                半生不熟
                熟了
                糊了
"""
class BBQ:
    # 初始化对象
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = '生的'
        self.condiments = []

    def __str__(self):
        #return '烤了' + str(self.cookedLevel) + '分钟,肉' + self.cookedString + '，调料有：' + str(self.condiments) + '。'
        msg = '烤了' + str(self.cookedLevel)
        msg += '分钟,肉' + self.cookedString
        if len(self.condiments)>0:
            msg += '，调料有：' #+ str(self.condiments) + '。'
            
            for i in self.condiments:
                msg += i + '，'

            msg = msg[:-1] + '。'
            # msg = msg.strip('，')
        else:
            msg += '，还没有添加调料。'
        return msg

    def cook(self, times):
        self.cookedLevel += times
        if self.cookedLevel < 3:
            self.cookedString = '生的'
        elif self.cookedLevel < 5:
            self.cookedString = '半生不熟'
        elif self.cookedLevel < 8:
            self.cookedString = '熟了'
        else:
            self.cookedString = '烤糊了'

    # def cook(self, times):
    #     self.cookedLevel += times
    #     if self.cookedLevel > 8:
    #         self.cookedString = '烤糊了'
    #     elif self.cookedLevel > 5:
    #         self.cookedString = '熟了'
    #     elif self.cookedLevel > 3:
    #         self.cookedString = '半生不熟'
    #     else:
    #         self.cookedString = '生的'
    
    def addCondiments(self, condiment):
        self.condiments.append(condiment)


bbq = BBQ()
print(bbq)

bbq.cook(1)
print(bbq)
bbq.addCondiments('芥末')
print(bbq)
bbq.cook(2)
print(bbq)
bbq.cook(2)
bbq.addCondiments('紫菜')
print(bbq)
bbq.cook(3)
bbq.addCondiments('孜然')
print(bbq)
bbq.cook(3)
print(bbq)