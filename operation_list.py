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



