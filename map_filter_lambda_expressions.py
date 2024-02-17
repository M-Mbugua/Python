def square(num):
    return num ** 2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))

def splicer(str):
    if len(str) % 2 == 0:
        return 'even'
    else:
        return str[0]

# names = ('Andy', 'Sam', 'Sally')
# list(map(splicer,names))

def check_even(num):
    return num % 2 == 0

# nums = (1,2,3,4,5,6)
# list(filter(check_even, nums))

square = lambda num : num ** 2

list(map(lambda num : num ** 2, my_nums))
list(filter(lambda num : num ** 2, my_nums))

names = ('Alice', 'Eve', 'Sally')
list(map(lambda x : x[::-1],names))