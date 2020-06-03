a=4*(6+5)
b=4*6+5
c=4+6*5
d=3+1.5+4
e=4**0.5
f=4**2
print("Numbers",a,"\t",b,"\t",c,"\n",d,"\t type of d=",type(d),"\t",e,"\t",f)
#strings
s='hello'
print("string ouputs",s[1],"\t",s[::-1],"\t",s[-1],"\t",s[4])
#lists
l=[0,0,0]
d=[]
d.append(0)
d.append(0)
d.append(0)
list3=[1,2,[3,4,'hello']]
list4 = [5,3,4,6,1]
list4.sort()
list3[2][2]='goodbye'
print("list outputs",l,"\t",d,"\t",list3,"\t",list4,)
#dicts
d={'simple_key':'hello'}
d1={'k1':{'k2':'hello'}}
d2={'k1':[{'nest_key':['this is deep',['hello']]}]}
d3={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print("dict=",d['simple_key'])
print(d1['k1']['k2'])
print(d2['k1'][0]['nest_key'][1][0])
print(d3['k1'][2]['k2'][1]['tough'][2][0])
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))
