# 附录

1. Git
使用Git做版本管理，阿里云的Code和Github都是很好的选择。若愿意将项目开源可选择Github，若私人或公司项目，则可以选择阿里云。Github国内访问速度会慢一点，但页面访问会更加便捷。
* [阿里云CODE](https://code.aliyun.com/)
  1. 注册账户
  2. 点击左侧目录：项目
  3. 新建项目
  4. 填写项目路径，可自定义项目组名称，如：pyprojects/python-study，可将多个关联项目放于同一组内；
  5. 可导入其他平台已有项目，此处我们只讲创建新项目
  6. 选择权限：Private（私有）或者 Public（公开）
  7. 创建项目并获取一个地址：git@code.aliyun.com:pyprojects/python-study.git
  8. 上传本地代码指令：
    * 全局设置
      ```
      git config --global user.name "dino"
      git config --global user.email "dino@dino.com"
      ```
    * 创建版本库
      ```
      git clone git@code.aliyun.com:pyprojects/python-study.git
      cd python-study
      touch README.md
      git add README.md
      git commit -m "add README"
      git push -u origin master
      ```
    * 已存在的目录或者仓库 
      ```
      cd existing_folder
      git init
      git remote add origin git@code.aliyun.com:pyprojects/python-study.git
      git add .
      git commit -m "版本描述"
      git push -u origin master
      ```
