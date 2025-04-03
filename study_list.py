languages = ['Java','python','ArkTS','Kotlin']
print(languages)

# 访问列表元素
print(f"列表的第一个元素是:{languages[0]}")

# 字符串的title方法，返回的是标准格式，小写变成大写
print(f"列表第二个元素，标准格式:{languages[1].title()}")

# 注意：Python中列表索引从0开始
print(f"列表最后一个元素是:{languages[-1]}")
# 倒数第二个元素：
print(f"列表倒数第二个元素是:{languages[-2]}")

# 修改列表元素,列表第一个元素修改为:JavaScript
languages[0] = "JavaScript"
print(languages)

# 在列表中添加元素，append方法，添加到末尾
languages.append('Swift')
print(languages)

# 在列表中插入数据,在列表的第二个位置上，插入数据
languages.insert(1,'C++')
print(languages)

# 从列表中删除元素,使用del语句删除
del languages[0]
print(languages)

# 使用pop()方法删除列表末尾元素
print(languages.pop())  # Swift
print(languages)


# 删除列表中任意位置的元素
del_language = languages.pop(0)
print(del_language)
print(languages)

# 根据值删除元素
languages.remove('ArkTS')
print(languages)


cars = ['bmw','toyota','audi','subaru']
# 使用sort对列表进行永久排序,按照字母顺序排序
cars.sort()
print(cars)

# 按照字母相反的顺序排序
cars.sort(reverse=True)
print(cars)

# sorted:对列表进行临时排序
cars = ['bmw','toyota','audi','subaru']
print(f"原始顺序:{cars}")
print(f"排列顺序:{sorted(cars)}")
print(f"排列之后:{cars}")


# 反向打印列表.反转列表的排列顺序
cars.reverse()
print(cars)

# 确定列表的长度，len
print(f"列表的长度为:{len(cars)}")
