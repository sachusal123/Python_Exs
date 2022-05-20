i=15
o=0
e=0
while i<=35:
    if i%2==0:
       o=o+i
    else:
       e=e+i
    i=i+1
print("Sum of even numbers=",o)
print("Sum of odd numbers=",e)