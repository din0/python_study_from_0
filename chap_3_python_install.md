# 第三章 Python安装

1. 版本问题
目前Python有两个主要版本，Python 2和Python 3，几乎所有的编程语言都会持续的优化迭代推出新的版本，在过度时作为使用者并不会有明显的不习惯。而Python是个特例，Python 2编写的代码在Python 3中可能无法正常运行。由于目前Python3是最新的主流版本，所以作为初学者，我们将不再涉及Python2的内容，当然在使用过程中如果有必要，会具体的讲解版本的区别。注意，python2的执行命令是：python，而python3的命令为：python3。

2. 不同系统中安装

* mac osx

  1). Python版本查看：

  ```python
  (base) localhost:~ dino$ python
  Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
  [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> exit()
  (base) localhost:~ dino$ python --version
  Python 3.7.6
  ```

  2). 安装Python3：
  * Homebrew本地安装，对于没有开发经验的朋友来说，我们需要了解一些常用的工具。[Homebrew](https://discourse.brew.sh/)是mac os下的一款软件包管理工具，详细介绍大家可以自行搜索。此处不再赘述。

    (1). 安装xcode命令行工具：

      ```python
      $ xcode-select --install
      ```

    (2). 安装Homebrew
    
      ```python
      $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      ```

    (3). 安装python3
      ```python
      $ brew install python3
      $ python3 --version
      ``` 

    (4). 测试python3：若可以正常返回“hello world!”即说明安装成功。
      ```python
      $ python3
      >>> print('hello world!')
      hello world!
      ```

    (5). 退出Python3
      ```python
      >>> exit()
      ```
      或者使用组合键：Control+D

  * 服务器安装：
    (1). 下载安装包：

      ```python
      $ mkdir pythonstudy
      $ cd pythonstudy
      $ wget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz
      ```

    (2). 解压缩
      ```python
      $ tar -zxvf Python-3.7.7.tgz
      ```

    (3). 安装
      ```
      $ cd /usr/local
      $ cd python-3.7.7
      $ 
      ```

  3). Python关键字和内置函数：
      Python关键字：注意不要使用关键字来自定义变量或者类名称。
      ```
      >>> help()
      help> keywords
      ```
      内置函数
      ```
      >>> dir(__builtins__)
      >>> help(int)   # 查看内置函数int的用法
      ```

3.终端运行
4.编辑器的使用
5.那些新手遇到的坑