"""
input函数:让程序暂停运行,等待用户输入一些文本。获取用户输入后,Python将其赋给一个变量，以便使用’
"""
#message = input('请输入相关信息：')
#print(message)


#name = input('please enter your name:')
#print(f"\nHello,{name}")


# int():输入的

age = input('你今年多大了：')
print(age)
if int(age)>=18:
    print("成年人")
else:
    print("未成年人")
