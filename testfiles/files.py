'''
text = "we are the world"

result = text.split()

print(result)
print(len(result))
'''
'''
def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            # print(len(contents))
    except FileNotFoundError:
        print("文件不存在")
        # pass
    else:
        words = contents.split()
        num_words = len(contents)
        print('文件' + filename + "有" + str(num_words) + "个字。")

# filename = 'ai.txt'
filenames = ['ai.txt','pi_digits.txt','guests.txt','hi.txt']
for filename in filenames:
    count_words(filename)
'''
'''
import json
num = [1,2,3,4,5,6,7]
# 写入到json文档
filename = 'numbers.json'
with open(filename,'w') as file_object:
    json.dump(num, file_object)

# 从json文档读取出来
with open(filename) as file_object:
    numbers = json.load(file_object)
print(numbers)
'''
'''
import json

username = input("请输入用户姓名：")

filename = 'username.json'

with open(filename,'w') as file_object:
    json.dump(username, file_object)
    print("您好，" + username + "!")

with open(filename) as file_object:
    username = json.load(file_object)
    print("欢迎回来，" + username + "!")
'''
import json
filename = 'username.json'

try:
    with open(filename) as file_object:
        username = json.load(file_object)
        # print("欢迎回来，" + username + "!")
except FileNotFoundError:
    username = input("请输入您的姓名：")
    with open(filename,'w') as file_object:
        json.dump(username, file_object)
        print("您好，" + username + "!")
else:
    print("欢迎回来，" + username + "!")