def vol_sphere(rad):
    return (4/3) * 3.142 * (rad ** 3)


def ran_check(num,low,high):
    if low <= num <= high:
        print(f'{num} is in the range between {low} and {high}')

    else:
        print(f'{num} is not in the range between {low} and {high}')


def check(num,low,high):
    if num in range(low, high+1):
        print(f'{num} is in the range between {low} and {high}')

    else:
        print(f'{num} is not in the range between {low} and {high}')



def up_low(str):
    lower_count = 0
    upper_count = 0

    for s in str:
        if s.isupper():
            upper_count += 1

        elif s.islower():
            lower_count += 1

        else:
            pass

    print(f'No of upper case characters : {upper_count}')
    print(f'No of lower case characters : {lower_count}')


def upper_lower(str):
    d = {'upper': 0, 'lower': 0}

    for s in str:
        if s.isupper():
            d['upper'] += 1

        elif s.islower():
            d['lower'] += 1

        else:
            pass

    print(f"Upper case characters : {d['upper']} and lower case characters : {d['lower']}")


def unique_list(lst):
    return list(set(lst))


def uniq_liat(lst):
    seen_numbers = []

    for num in lst:
        if num not in seen_numbers:
            seen_numbers.append(num)

    return seen_numbers


def multiply_list(lst):
    result = 1

    for i in range(len(lst)):
        result = result * lst[i]

    return result


def palindrome(s):
    return s == s[::-1]



import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str2 = str1.lower().replace(" ", "")
    count = 0

    for letter in alphabet:
        if letter in str2:
            count += 1

        else:
            pass

    return count == 26

def ispangram(str1, alphabet=string.ascii_lowercase):
    set_str1 = set(str1.lower().replace(" ", ""))
    alphaset = set(alphabet)

    return set_str1 == alphaset
