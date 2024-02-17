def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] ==3:
            return True
    return False


def paper_doll(text):
    result = ''
    for item in text:
        result += item * 3

    return result


def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif sum([a,b,c]) > 31 and 11 in [a,b,c]:
        return sum([a,b,c]) - 10
    else:
        return 'BUST'


def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False

        while not add:
            if num != 9:
                break
            else:
                add = True
                break

    return total


def spy_game(nums):

    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


def count_primes(num):
    if num < 2:
        return 0

    # store prime numbers, 2 is prime that's why it is already added
    primes = [2]

    # counter going up to the input number, we start at 3
    x = 3

    while x < num:
        # take steps of 2 because all even numbers except 2 are not prime
        # check whether x is prime
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)






