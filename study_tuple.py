# 列表是可以修改的，元组是不可修改的，不可变的列表称之为元组tuple

# 定义元组，使用圆括号定义元组，使用索引来访问其中的元素，就像列表一样

widths = (10,20,30,45,32)
# 访问元组中值
print(widths[0])
print(widths[3])

# 注意：元组中的元素不可修改

# 遍历元组的值
for width in widths:
    print(width)

print("--------")

# 虽不能修改元组中的元素，但可以给元组变量重新赋值
widths = (10,20)
# 遍历元组的值
for width in widths:
    print(width)
