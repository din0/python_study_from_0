# 第十三章 数据可视化

1. 安装 matplotlib

$ pip3 install --user matplotlib
>>> import matplotlib

2. 测试

>>> import matplotlib.pyplot as plt
>>> squares = [1,4,9,15,26]
>>> plt.plot(squares)
[<matplotlib.lines.Line2D object at 0x119bcd050>]
>>> plt.show()

sample:

随机漫步
random_walk.py
