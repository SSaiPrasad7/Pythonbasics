# Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (4 / 3) * (3.14) * (rad ** 3)


print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    if low <= num <= high:
        return True, f"{num} is in the range between {low} and {high}"
    return False


print(ran_check(5, 2, 7))


# Write a Python function that calculates the number of upper case letters and lower case letters in a string.

def up_low(s):
    uppercasecount = 0
    lowercasecount = 0
    for i in s:
        if i.isupper():
            uppercasecount += 1
        elif i.islower():
            lowercasecount += 1
    return uppercasecount, lowercasecount


print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    m = 1
    for i in numbers:
        m *= i
    return m


print(multiply([1, 2, 3, -4]))


# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]


print(palindrome('nurses run'))


# Write a Python function to check whether a string is pangram or not.


def ispangram(str1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char in str1.lower():
            return True

    return False

print(ispangram("The quick brown fox jumps over the lazy dog"))