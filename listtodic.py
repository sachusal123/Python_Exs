list1=[]
list2=[]
list1_tot=int(input("Enter total no of elements in list 1"))
i=0
while i<list1_tot:
    it=int(input("Enter  Item:"))
    list1.append(it)
    i=i+1
list2_tot=int(input("Enter total no of elements in list 2"))
i=0
while i<list2_tot:
    it=int(input("Enter  Item:"))
    list2.append(it)
    i=i+1

print("List 1=",list1)
print("List 2=",list2)
dict_1= dict(zip(list1,list2))
print(dict_1)