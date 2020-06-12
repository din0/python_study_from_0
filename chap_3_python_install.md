# 第三章 Python安装

1. 版本问题
目前Python有两个主要版本，Python2和Python3，几乎所有的编程语言都会持续的优化迭代推出新的版本，在过度时作为使用者并不会有明显的不习惯。而Python是个特例，Python2编写的代码在Python3中可能无法正常运行。由于目前Python3是最新的主流版本，所以作为初学者，我们将不再涉及Python2的内容，当然在使用过程中如果有必要，会具体的讲解版本的区别。截止到目前，最新发布的版本是3.8.2。
注意，python2的执行命令是：python，而python3的命令为：python3。

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

* Windows
  去[Python官网](https://www.python.org/downloads/windows/) 下载.exe安装包，一定要选择系统对应的安装包版本，直接双击安装；安装时需要记住python的安装位置。
  ​注意，在第一个安装界面，要选中“Add Python 3.X to PATH”，这样在安装完成后便不需要设置路径，可以直接运行python.exe执行命令行窗口。

  * 服务器安装：后面我们会单独讲解如何部署服务器环境

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

3.1 Mac下，我们可以在终端里输入​：python3，当看到版本号以及 >>> 时表示已经进入python命令行。

    ```python
    (base) localhost:~ dino$ python3
    Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
    [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

3.2 Windows下可以在安装位置找到python.exe文件，双击打开，即可看到python​运行窗口，输入并执行命令即可。


4.编辑器的使用

目前主流的编辑器基本上都支持Python，大家可以选择自己​习惯的。这里我们重点介绍两款，

4.1 VS Code，几乎覆盖所有主流编程语言，插件丰富，免费。[下载地址](https://code.visualstudio.com/)

4.2 Pycharm，专为Python开发使用的编辑器，安装即有环境，但只有社区版是免费的。[下载地址](https://www.jetbrains.com/zh-cn/pycharm/promo/)

4.3 Anaconda运行环境的Jupyter，这个我们后面讲到虚拟环境的时候再说吧。
