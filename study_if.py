# 一个简单的示例
cars = ['bmw','toyota','audi','subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


car = 'bmw'
print(car == 'bmw') # True
print(car == 'audi') # False

# 不等运算符 !=

# 检查多个条件
# and：每个条件都通过了，整个表达式为True，如果至少一个条件没通过，就为False
# or：其中一个条件通过了，整个表达式为True，否则为False

age_student_A = 25
age_student_B = 28

print("------1")

if age_student_A >=25 and age_student_B >=28:
    print(True)
else:
    print(False)
print("------2")

if age_student_A >=26 or age_student_B >=30:
    print(True)
else:
    print(False)


print("------3")
# 检查特定值是否在列表中

"""
in:在列表中
not in:不在列表中
"""
cars = ['bmw','toyota','audi','subaru']

# 在列表中
print('bmw' in cars)
# 不在列表中
print('byd' not in cars)


# if语句
age = 17;
if age>=18:
    print("成年人")

# if-else语句
if age>=18:
    print("成年人")
else:
    print("未成年人")


# if-elif-else

if age>=18 and age<=45:
    print("青年人")
elif age>=46 and age<=60:
    print("中年人")
elif age>60:
    print("老年人")
else:
    print("未成年人")