# WARMUP SECTION
# LESSER OF TWO EVENS
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        if a > b:
            return a
        else:
            return b


print(lesser_of_two_evens(2, 5))


# ANIMAL CRACKERS
def animal_crackers(s):
    a = s.split()
    if a[0][0] == a[1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'), animal_crackers('Crazy Kangaroo'))


# MAKES TWENTY
def makes_twenty(n1, n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10), makes_twenty(12, 8), makes_twenty(2, 3))


##############################################
# LEVEL 1 PROBLEMS
# OLD MACDONALD
def old_macdonald(name):
    n1 = name[:3]
    n2 = name[3:]
    return n1.capitalize() + n2.capitalize()


print(old_macdonald('macdonald'))


# MASTER YODA
def master_yoda(text):
    t = text.split()
    t.reverse()
    return " ".join(t)


print(master_yoda('I am home'), "\t", master_yoda('We are ready'))


# ALMOST THERE
def almost_there(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False


print(almost_there(90), almost_there(104), almost_there(150), almost_there(209))


#########################################
# LEVEL 2 PROBLEMS
# FIND 33
def has_33(nums):
    sa = ''.join(map(str, nums))
    if sa.find('33') != -1:
        return True
    else:
        return False


print(has_33([1, 3, 3]), has_33([1, 3, 1, 3]), has_33([3, 1, 3]))


# PAPER DOLL
def paper_doll(text):
    t = ''
    for i in text:
        t += i * 3
    return t


print(paper_doll('Hello'), "\t", paper_doll('Mississippi'))


# BLACKJACK
def blackjack(a, b, c):
    if a + b + c <= 21:
        return a + b + c
    elif a == 11 or b == 11 or c == 11:
        return (a + b + c) - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 7), blackjack(9, 9, 9), blackjack(9, 9, 11))


# SUMMER OF '69
def summer_69(arr):
    sum = 0
    for val in arr:
        if val in [6,7,8,9]:
        #if val == 6 or val == 7 or val == 8 or val == 9:
            continue
        sum += val
    return sum


print(summer_69([1, 3, 5]), summer_69([4, 5, 6, 7, 8, 9]), summer_69([2, 1, 6, 9, 11]))


#######################################
# CHALLENGING PROBLEMS
# SPY GAME
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for i in nums:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]), spy_game([1, 0, 2, 4, 0, 5, 7]), spy_game([1, 7, 2, 0, 4, 5, 0]))


# COUNT PRIMES
def count_primes(num):
    count = 0
    l = []
    for n in range(2, num):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            count += 1
            l.append(n)
    return count, l


print(count_primes(100))
