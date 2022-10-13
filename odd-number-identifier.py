o=[]
p=[]
y=0
x=int(input("how many numbers you want to enter in list="))
while y<x:
    a=int(input("enter no."))
    o.append(a)
    a=0
    y+=1
print("list=",o)
for i in range(0,x):
    b=o[i]%2
    if b!=0:
        p.append(o[i])
print("odd no.=",p)
print("goodbye")
