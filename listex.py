L=[2,1,32]
M=[47,25]
L=L+M
L.pop(3)
L.sort()
L.append("sai")
L.reverse()
k=len(L)
print("After List ops: ",L,"\nlength of the string= ",k)
s=[L,M,[938,234,543],[2.3,[45.3,3.6],756.9],["sad","sorry","shame"]]
print('Nested lists', s[3][-2][0])