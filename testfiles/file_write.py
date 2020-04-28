'''
调用open() 时提供了两个实参（见❶）。
第一个实参也是要打开的文件的名称；第二个实参（'w' ）告诉Python，
我们要以写入模式写入模式 打开这个文件。
打开文件 时，可指定读取模式读取模式 （'r' ）、写入模式写入模式 （'w' ）、
附加模式附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）。
如果你省略了模式实参，Python将以默认的只读模式打 开文件。
'''
"""
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    msg = "I love programming.\n"
    msg += "我正在学习Python语言。\n"
    
    file_object.write(msg)
"""

filename = 'guests.txt'
with open(filename, 'a') as file_object:
    name = " "
    names =[]
    while name != "":
        name = input("请输入顾客姓名：")
        file_object.write(name + '\n')
        names.append(name)
    else:
        # names.remove("quit")
        print("Goodbye!")
    print(','.join(names))