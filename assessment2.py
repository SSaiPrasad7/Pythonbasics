#1
st = 'Print only the words that start with s in this sentence'
x=st.split()
for i in x:
    if(i[0]=='s'):
        print(i)
'''
while i<len(x):
    if(x[i][0]=='s'):
        print(x[i])
    i+=1
'''
#2
list2=list(range(0,11,2))
print(list2)
'''
for i in range(0,11):
    if(i%2==0):
        print(i)

'''
#3
mylist=[x for x in range(1,51) if x%3==0]
print(mylist)
#4
st1 ='Print every word in this sentence that has an even number of letters'
a=st1.split()
for y in a:
    if len(y)%2==0:
        print("even",y)
#5
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print('FizzBuzz')
    elif(i%5==0): 
        print('Buzz')
    elif(i%3==0):
        print('Fizz')
    else:
        print(i)
#6
st3 = 'Create a list of the first letters of every word in this string'
b=st3.split()
mylist2=[x[0] for x in b]
print(mylist2)
