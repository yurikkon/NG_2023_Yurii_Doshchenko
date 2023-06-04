ready_list = []
user_list = []

for i in range(3):
    buffer_list = input("Enter a list of elements separated by spaces: ").split()
    user_list.append(buffer_list)

for input_list in user_list:
    buffer_list = []
    for element in set(input_list):
        if input_list.count(element) > 1:
            buffer_list.extend(element)
    ready_list.extend(set(buffer_list))
print(set(ready_list))