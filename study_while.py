prompt = "\nTell me something"
prompt += "\nEnter quit to end:"

"""
message = ""
while message != "quit":
    message = input(prompt)
    print(message)
"""

# break:退出整个循环
# continue：退出当前循环，继续下次循环

# 打印出1-10中所有奇数：
current_num = 0
while current_num < 10: 
    current_num += 1 
    if current_num % 2 == 0:
        continue
    print(current_num)

# 使用while 循环处理列表和字典

# 在列表之间移动元素

unconfirmed_users = ['alice' , 'jim' , 'bob']
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"Verifing user:{current_users.title()}")
    confirmed_users.append(current_users)
    print("\nThe following been verfied")
    for confirmed_user in confirmed_users:
        print(confirmed_user)


# 删除为特定值的所有列表
pets = ['dog','cat','dog','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)



