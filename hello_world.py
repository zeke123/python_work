print("hello python world")

print("第二行代码")

# 变量命名规则：
"""
1、变量名只能包含字母、数字和下换线,不能以数字开头
2、变量名不能包含空格
3、不能用Python中的关键字、函数作为变量名
4、变量名既要简短有要具有描述性
5、慎用小写字母i和大写字母O
"""

# 字符串：可以是单引号，也可以是双引号

name="zhoujian"
print(name.title()) #Zhoujian,将姓名设置为合适的格式
print(name.upper()) #ZHOUJIAN
print(name.lower()) #zhoujian

# f字符串
first_name = "zhou"
last_name = "jian"
full_name = f"{first_name}{last_name}"
print(full_name)
print(f"hhello,{full_name}")

# 制表符和换行符
# 字符串中添加制表符，\t
print("\tPython")
print("Python")

# 换行符，\n

print("language:\nJava\nPython\nArkTS")

# 同时制表符和换行符 \n\t

print("\n\tlanguage:\n\tJava\n\tPython\n\tArkTS")

language = " python "
print(language.lstrip()) # 删除左边空白
print(language.rstrip()) # 删除右边空白
print(language.strip()) # 删除左右两边的空白