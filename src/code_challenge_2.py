from stack import Stack


def find_minimum(stack):
    value_list = []
    current_value = ''
    try:
        while current_value is not None:
            current_value = stack.pop()
            value_list.insert(0, current_value)
    except ValueError:
        print(value_list)
        for value in value_list:
            stack.push(value)
            filtered_list = [x for x in value_list if x is not None]
        return min(filtered_list)


new_stack = Stack((45, 46, 47, 48))
print(find_minimum(new_stack))
print(find_minimum(new_stack))
print(find_minimum(new_stack))
