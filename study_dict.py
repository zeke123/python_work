
"""
Python中的字典:
是一系列键值对,每一个键都与一个值相关联,Python中,字典使用{}

"""

my_dict = {'name': 'zhoujian', 'age': 37, 'city': 'nanjing'}

# 访问字典中的值
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['city'])

# 添加键值对
my_dict['height'] = "174cm"
my_dict['weight'] = "62kg"
print(my_dict)

# 创建一个空字典
person_dict = {}

# 添加键值对
person_dict['age'] = 18
person_dict['city'] = "shanghai"
print(person_dict)


# 修改字典中的值
person_dict['age'] = 28
person_dict['city'] = "nanjing"
print(person_dict)


# 删除键值对,使用del语句删除
del person_dict['age']
print(person_dict)




