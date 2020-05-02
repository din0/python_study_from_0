"""
随机漫步
"""
from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        # 初始化属性
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # 计算所有的点，漫步循环，直到遍历所有的点数
        while len(self.x_values) < self.num_points:
            #决定前进的方向以及沿着这个方向前进的距离
            x_direction = choice([1,-1])        #选择方向，1向右走，-1向左走
            x_distance = choice([0,1,2,3,4])    #随机选择一个0-4之间的整数，告诉走多远
            x_step = x_direction * x_distance   #移动方向*移动距离，已确定沿x和y轴移动的距离，

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #禁止原地重复点
            if x_step == 0 and y_step == 0:
                continue
            
            #计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            