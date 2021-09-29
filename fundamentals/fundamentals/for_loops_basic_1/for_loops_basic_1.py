# print all integers 0 to 150
for i in range(151):
    print(i)

# print all multiples of 5 from 5 to 1000
for i in range(5,1001,5):
    print(i)

# count the dojo way
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# whoa that sucker's huge!
sum = 0
for i in range(500001):
    if i % 2 != 0:
        sum += i
print(sum)

# countdown by fours
count = 2018
while count > 0:
    print(count)
    count -= 4

# flexible counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)