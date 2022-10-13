o=[]
p=[]
y=0
x=int(input("How many numbers you want to enter in list="))
while y<x:
    a=int(input("Enter a number:"))
    o.append(a)
    a=0
    y+=1
print("list=",o)
for i in range(0,x):
    b=o[i]%2
    if b!=0:
        p.append(o[i])
print("Odd number=",p)
print("Goodbye")
