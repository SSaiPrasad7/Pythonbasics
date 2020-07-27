def func(num,n):
    list1 = []
    dict1={}
    str1=""
    for i in range(10,36,1):
            dict1[i]=chr(i+55)
    while True:
        rem=int(num%n)
        list1.append(rem)
        num = num/n
        if num==0:
            break
    for i in range(len(list1)):
        for j in dict1:
            if list1[i]==j:
                list1[i]=dict1[j]
    list1.reverse()
    print("".join(map(str,list1)))



func(891,5)
