filename = 'pi_digits.txt'
with open(filename) as file_object:
    # contents = file_object.read()
    # print(contents.strip())
    #逐行读取
    # for line in file_object:
        # print(line)

    #创建一个包含内容的列表
    lines = file_object.readlines()
    
# for line in lines:
#     print(line.strip())
# print(lines)

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
birthday = input("输入你的生日mmddYY：")
if birthday in pi_string:
    print("你的生日在PI里！")
else:
    print("你的生日不在PI里！")

