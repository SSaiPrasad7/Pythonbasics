import random


def gensquares(N):
    for i in range(N):
        yield i ** 2


for x in gensquares(10):
    print(x)

print("\n")
def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)


for num in rand_num(1,10,12):
    print(num)


s="hello"
print(next(iter(s)))