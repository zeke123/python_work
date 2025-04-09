class Dog:
    def __init__(self,name,age):

        """
         __init__方法是一个特殊方法,每次创建Dog实例时,Python会自动运行
         参数：
         self:必不可少，自动传入
         name:名字
         age:年龄
         self.name = name:通过类的实例来访问
         初始化属性:name/age
        """
        self.name = name
        self.age = age
    
    def sit(self):
        """小狗坐下"""
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        """小狗打滚"""
        print(f"{self.name} rolled over!")

# 创建实例
my_dog = Dog("Willie",3)

# my_dog.name:访问属性
print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

# 调用方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog("Lucy",6)
print(f"Your dog name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()



        