# 定义函数使用def关键字
# name是形参
# zhoujian是实参
def greet_user(name):
    print(f"hello {name}")

greet_user('zhoujian')

# 关键字实参
def descripe_pet(animal_type,animal_name):
    print(f"animal_type is {animal_type}")
    print(f"animal_name is {animal_name}")

descripe_pet(animal_type = 'hamster',animal_name = "harry")

# 默认值
def descripe_pet(animal_type,animal_name = 'dog'):
    print(f"animal_type is {animal_type}")
    print(f"animal_name is {animal_name}")

# 返回值
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name}{last_name}"
    return full_name.title()

print(get_formatted_name('zhou','jian'))

# 返回字典
def build_person(first_name,last_name):
    person = {'first_name':first_name,'last_name':last_name}
    return person

person_new = build_person('zhou','jian')
print(person_new)


# 结合使用函数和while循环

def get_formatted_name(first_name,last_name):
    full_name = f"{first_name}{last_name}"
    return full_name.title()


# 无线循环
while True:
    print("\nPlease tell me your name:")
    first_name = input("First Name:")
    if first_name == 'q':
        break

    last_name = input("Last Name:")
    if last_name == 'q':
        break

    name = get_formatted_name(first_name,last_name)
    print(f"\nHello {name}")

 # 传递列表
def greet_users(names):
    for name in names:
        msg = f"hello {name.title()}"
        print(msg)

usernames = ['jim','jack','bob']
greet_users(usernames)


# 在函数中修改列表



   

