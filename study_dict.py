
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

# 使用get方法来访问值
my_dict = {'name': 'zhoujian', 'age': 37, 'city': 'nanjing'}

# "na"不存在，会报错
#print(my_dict['na'])
# 使用get
# 不存在，直接返回None，不会报错
print(my_dict.get('na')) #None
print(my_dict.get('na',"这个键不存在")) # 这个键不存在

# 遍历字典
for key,value in my_dict.items():
    print(f"key:{key}")
    print(f"value:{value}")

print("-------1")

# 遍历字典中所有的键
for key in my_dict.keys():
    print(key)
print("-------2")
# 遍历字典中所有的值
for value in my_dict.values():
    print(value)

print("-------3")
# 按照特定顺序遍历字典中的所有键
for key in sorted(my_dict.keys()):
    print(key)

print("-------4")

# 字典列表
person_a_dict = {'name': 'zhangsan', 'age': 37, 'city': 'nanjing'}
person_b_dict = {'name': 'lisi', 'age': 32, 'city': 'shanghai'}
person_c_dict = {'name': 'wangwu', 'age': 27, 'city': 'hangzhou'}

persons = [person_a_dict,person_b_dict,person_c_dict]
for person in persons:
    print(person)

print("-------5")
# 在字典中存储列表
mine_dict = {'name': 'zhoujian', 'age': 38, 'city': 'nanjing',"languages":["Java","Python","ArkTS"]}

# 遍历字典中的键
for key in mine_dict.keys():
    print(key)

print("-------6")

# 遍历字典中的值
for value in mine_dict.values():
    print(value)

print("-------7")

# 遍历字典
for key,value in mine_dict.items():
    print(key)
    print(value)

print("-------8")

# 在字典中存储字典
users_dict = {"xiaoming":{"weight":"80kg","height":"179cm","city":"beijing"},"xiaohong":{"weight":"50kg","height":"165cm","city":"shanghai"}}
for name,person_info in users_dict.items():
    print(name)
    print(person_info)
    city = person_info['city']
    print(city)






