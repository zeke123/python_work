# 使用as给函数指定别名
# 从模块pizza.py中导入make_pizza函数，给make_pizza函数指定别名为mp

from pizza import make_pizza as mp

# 函数别名 make_pizza-->mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
