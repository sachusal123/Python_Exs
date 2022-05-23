n=int(input ("Enter total number of items in the list:"))
a=[]
i=0
while i<n:
    it=int(input("Enter  Item:"))
    a.append(it)
    i=i+1
print("List is :",a)
i=0
print("Numbers that were divisible by 5 are::")
while i<n:
    if a[i]%5==0:
        print(a[i])
    else:
        pass
    i=i+1