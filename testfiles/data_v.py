import matplotlib.pyplot as plt

'''
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_values, squares, linewidth=5)

plt.show()
'''

'''
使用scatter()绘制散点图并设置样式
'''
'''
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values = list(range(1,101))
y_values = [x**2 for x in x_values]

# edgecolor = 'none' 去掉圆点边缘的黑色, c = 'red' / (0,0,0.8) 是圆点颜色
# plt.scatter(x_values, y_values, c='red', edgecolor = 'none', s=20)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor = 'none', s=20)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize = 14)

# 展示图表文件
# plt.show()

# 保存图表文件
plt.savefig('squares_plot.png', bbox_inches='tight')
'''

"""
随机漫步
创建RandomWalk()类存于 random_walk.py 中
"""

from random_walk import RandomWalk

while True:
    #创建RandomWalk实例并绘制点
    rw = RandomWalk(10000)
    rw.fill_walk()
    #设置窗口尺寸,figure()用于指定宽高分辨率和背景色，用元组来设定。
    # plt.figure(dpi=128, figsize=(10,6))
    #获取点数
    point_numbers = list(range(rw.num_points))
    #定义样式
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor = 'none', s=10)
    plt.title("Random Walk", fontsize = 20)
    plt.xlabel("X Value", fontsize = 14)
    plt.ylabel("Y Value", fontsize = 14)
    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolor='none', s=50)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=50)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #显示图表
    plt.show()

    #模拟多次随机漫步
    keep_running = input("加载下一次？(y/n):")
    if keep_running == 'n':
        break
