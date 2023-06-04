string = input("Enter elements through a space: ").split(" ")
anything = input("Enter anything: ")
count = 0
for char in string:
    if char == anything:
        count += 1
print(f"Number of occurrences of '{anything}': {count}")

