

# 指定参数middle_name为空字符串，变成可选参数
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""

    # 如果middle_name不为空，返回true，否则false
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)