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

#

