

# 给参数指定默认值
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 传参时，也可以指定参数名
describe_pet(pet_name='willie')
