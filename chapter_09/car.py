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
    

    
    
my_car = Car('audi','a8',2025)
full_name = my_car.get_full_name()
print(full_name)

# 读取行驶里程数
my_car.read_odometer()

# 修改属性值
my_car.odometer_reading = 50
my_car.read_odometer()

# 修改属性值
my_car.update_odometer(100)
my_car.read_odometer()





