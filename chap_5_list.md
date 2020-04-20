# 第五章 列表 LIST

list=[]
names=['tom','jimmy','john']
names.append('dino')
names
['tom', 'jimmy', 'john', 'dino']

for i in range(len(names)):
  print(names[i])
  list.append(names[i])

list
['tom', 'jimmy', 'john', 'dino']

列表末尾添加：append()
列表开头插入：insert()

删除元素：del list[i]
pop()

删除列表值：remove()

