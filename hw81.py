def chop(my_list):
    if len(my_list) >= 2:
        del my_list[0]
        del my_list[-1]
    else:
        my_list.clear()
    return None

def middle(my_list):
    if len(my_list) >= 3:
        return my_list[1:-1]
    else:
        return []

# Sample usage
my_list = [1, 2, 3, 4]

print("my list before call chop function =>", my_list)
chop(my_list)
print("my list after call chop function =>", my_list)

my_list = [1, 2, 3, 4]

print("\nmy list before call middle function =>", my_list)
new_list = middle(my_list)
print("my list after call middle function =>", my_list)
print("new list after call middle function =>", new_list)