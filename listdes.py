list1_no=int(input("Enter Total no of elements in the list:"))
print("Enter",list1_no,"Elements")
list1=[]
i=0
while i<list1_no:
    item=int(input("Enter the item:"))
    list1.append(item)
    i=i+1
j=0
temp=0
print(list1[j])
while list1[j]>list1[j+1]:
      temp=list1[j]
      list1[j]=list1[j+1]
      list1[j+1]=temp
print(list1)