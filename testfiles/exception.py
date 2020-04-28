# print(5/0)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("被除数不可以为0.")

# 除法计算器
print("输入两个数字，将执行除法。")
print("输入q退出。")

while True:
    num_1 = input("请输入第一个数字：")
    if num_1 == 'q':
        break
    num_2 = input("请输入第二个数字：")
    if num_2 == 'q':
        break
    try:
        result = int(num_1)/int(num_2)
    except ZeroDivisionError:
        print("被除数不能为0！")
    else:
        print(result)