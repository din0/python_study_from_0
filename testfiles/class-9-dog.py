"""
《python编程：从入门到实践》中第九章练习
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        # 动作：坐下，得到指令时坐下
        print(self.name + "坐下")

    def roll_over(self):
        print(self.name + "打滚")

dog = Dog("皮蛋", "2")
print("我有一只狗叫" + dog.name + "它已经" + str(dog.age) + "岁了。")
dog.sit()
dog.roll_over()

print("===============================分隔符===============================")

class Restaurant:
    def __init__(self, res_name, cuisine_type):
        self.name = res_name
        self.type = cuisine_type
    
    def describ_restaurant(self):
        print(self.name + "是一间" + self.type + "餐厅。")

    def open_restaurant(self):
        print("餐厅正在营业。")

class IceCream(Restaurant):
    def __init__(self, res_name, cuisine_type):
        super().__init__(res_name, cuisine_type)
        # self.flavors = "apple"

    def flavors(self):
        flavors = ['香草','巧克力','草莓']
        print(self.name + "的冰淇淋口味有：" + ','.join(flavors))

res = Restaurant("KFC", "快餐")
res.describ_restaurant()
res.open_restaurant()
ic = IceCream("哈根达斯", "冰淇淋店")
ic.flavors()

print("===============================分隔符===============================")

class User:
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name
    
    def describ_user(self):
        print("当前客户是：" + self.firstName.title() + " " + self.lastName.title())
    
    def great_user(self):
        print(self.firstName.title() + " " + self.lastName.title() + " 是个很有名的演员！")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
        msg = self.firstName + " " + self.lastName
        print(msg)

class Privileges():
    privileges = ['添加', '删除', '编辑']
    def show_privileges(self):
        # msg = self.firstName + " " + self.lastName
        msg = "作为管理员的权限有：" + ','.join(self.privileges)
        print(msg)

user = User("tom", "cruise")
user.describ_user()
user.great_user()
admin = Admin("文翔","张")
# admin.show_privileges()
admin.privileges.show_privileges()

print("===============================分隔符===============================")

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        # 添加里程数
        self.current_mileage = 0
        # self.gastank = gastank
    
    def carInfo(self):
        msg = "我的车是一辆" + self.year + "年的" + self.brand + self.model + "汽车"
        print(msg)
    
    #当前里程数
    def mileAge(self):
        msg = "当前车辆的里程数为：" + str(self.current_mileage) + " 公里。"
        print(msg)

    #今天新增里程数
    def todayMileage(self, mileage):
        if mileage>= self.current_mileage:
            self.current_mileage = mileage
        else:
            print("里程表不可以回拨。")
    
    def increment_odometer(self, miles):
        print("我今天跑了" + str(miles) + "公里。")
        self.current_mileage += miles

    def gastank(self):
        print("我的油箱容积")

#定义子类用来继承父类Car中的方法
class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        # self.battery = 300
        self.battery = Battery()
    
    def batteryInfo(self):
        print("当前电池容量为：" + str(self.battery))

    def gastank(self):
        # return super().gastank()
        print("电动汽车没有油箱。")

class Battery():
    def __init__(self, battery_size = 200):
        self.battery_size = battery_size
        
    def batteryCap(self):
        print("这辆车的电池容量是：" + str(self.battery_size))

    def get_range(self):
        if self.battery_size == 202:
            range = 450
        elif self.battery_size == 300:
            range = 550
        msg = "可以行驶里程为：" + str(range)
        print(msg)
    #电池升级
    def upgrade_battery(self):
        if self.battery_size < 202:
            self.battery_size = 202
        # print("这辆车升级后的电池容量是：" + str(self.battery_size))

my_car = Car("丰田", "汉兰达", "2018")
my_car.carInfo()
# my_car.mileage = 100
my_car.increment_odometer(200)
my_car.mileAge()
my_car.increment_odometer(300)
my_car.mileAge()
my_car.gastank()

my_tesla = ElectricCar("特斯拉", "Model3", "2019")
my_tesla.carInfo()
# my_tesla.batteryInfo()
my_tesla.gastank()

my_tesla = ElectricCar("特斯拉", "Model S", "2017")
my_tesla.carInfo()
my_tesla.battery.batteryCap()

my_tesla.battery.upgrade_battery()
my_tesla.battery.batteryCap()
# my_tesla.battery.get_range()



print("===============================分隔符===============================")

