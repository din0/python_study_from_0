# 第十二章 文件和异常

1. 文件中读取数据

    ```python
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents.strip())
    ```

    绝对路径：

    ```python
    path = '/.../...'
    ```

2. 写入文件

    ```python
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
    ```

3. 异常

    ```python
    try:
        statements
    expert ZeroDivisionError:
        print("被除数不能为0！")
    ```

    ```python
    filename = 'alice.txt'
    try:
        with open(filename) as f_obj:
            contents = f_obj.read() 
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    ```

4. 文本分析

    ```python
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
    ```

5. 存储数据：使用JSON来存储用户数据

    json.dump() 存储数据
    json.load() 加载数据

    ```python
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
    ```

    ```python
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
    ```

6. 使用函数重构代码
