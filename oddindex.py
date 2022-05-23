n=int(input("Enter total number of list of items:"))
list1=[]
list2=[]
i=0
while i<n:
    item=int(input("Enter item:"))
    list1.append(item)
    i=i+1
i=1
while i<n:
    if i%2==0:
       pass
    else:
        list2.append(list1[i])
    i=i+1
print(list1,list2)