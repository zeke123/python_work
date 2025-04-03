languages = ['Java','python','ArkTS','Kotlin']

# for循环
for language in languages:
    print(language)
    print(f"{language} is the best language")

# range()函数：rang(1,5)生成1~5，不包括5

for value in range(1,5):
    print(value)

# 使用range函数创建值列表
# 可以使用list函数，将range函数的结果转化为列表
numbers = list(range(1,6))
print(numbers)

numbers = []
for number in range(1,11):
    numbers.append(number**3)
print(numbers)

# 对列表进行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,10]
print(f"列表中最小的值为:{min(digits)}")
print(f"列表中最大的值为:{max(digits)}")
print(f"列表中所有元素总和为:{sum(digits)}")

# 列表推导式：就是将for循环的的多行代码合并成一行
"""
将以下代码：
numbers = []
for number in range(1,11):
    numbers.append(number**3)
print(numbers)

改成一行
"""

# 列表推导式
numbers = [number**3 for number in range(1,11)]
print(numbers)

# 使用列表的一部分：切片slice
languages = ['Java','python','ArkTS','Kotlin']

# 输出一个列表，包含前三种语言

# [0:3]返回索引分别为0、1、2的元素
print(languages[0:3])

# [1:3]返回索引分别为1、2的元素
print(languages[1:3])

# 如果没有指定第一个索引，Python将自动从列表开头开
print(languages[:2])

# 如果没有指定最后的索引，切片终止于列表末尾
print(languages[1:])

# 打印列表中的最后的2个元素：languages[-2:]
print(languages[-2:])

# 遍历切片
# 遍历languages列表中的前三种语言
for language in languages[0:3]:
    print(language)

print("----------")

# 遍历最后两种语言
for language in languages[-2:]:
    print(language)





