"""
继承:子类继承父类，子类将自动获取父类的所有属性和方法，子类也可以定义自己的属性和方法。

下面编写电车:ElectricCar,继承Car
"""

class Car:
    def __init__(self,make,model,year):
        # 品牌
        self.make = make
        # 型号
        self.model = model
        # 年份
        self.year = year
        # 给属性指定默认值，行驶里程为0
        self.odometer_reading = 0

    def update_odometer(self, mileage):
         """通过方法修改行驶里程数"""
         if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
         else:   
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """读取行驶里程数"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def get_full_name(self):
        """获取完整信息"""
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    


# 子类ElectricCar继承父类Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)

        # 给子类定义属性
        self.battery_size = 30

    # 给子类定义方法
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    

# 直接调用父类的方法
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_full_name())

# 调用子类的方法
my_leaf.describe_battery()