# countdown
def countdown(num):
    lst = []
    while num >= 0:
        lst.append(num)
        num -= 1
    return lst

print(countdown(5))

# print and return
def print_and_return(lst):
    print(lst[0])
    return lst[1]

print_and_return([1,2])

# first plus length
def first_plus_length(lst):
    sum = lst[0]
    sum += len(lst)
    return sum

first_plus_length([1,2,3,4,5])

# values greater than second
def greater_than_second(lst):
    new_list = []

    if len(lst) < 2:
        return False
    
    for item in lst:
        if item > lst[1]:
            new_list.append(item)
    
    print(len(new_list))
    return new_list

greater_than_second([5,2,3,2,1,4])
greater_than_second([3])

# this length, that value
def size_value(size, value):
    lst = []
    for i in range(size):
        lst.append(value)
    return lst

size_value(4,7)
size_value(6,2)