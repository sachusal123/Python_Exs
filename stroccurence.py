str1=input("Enter a string:")
list1=[]
str1_split=str1.split()
str1_length=len(str1_split)
for a in str1_split:
    c=0
    for b in str1_split:
        if a==b:
            c=c+1
    print("Occurances of",a,"is",c)
    list1.append(c)
list2=list(str1_split)
list3=list(list1)
list2_d=set(list2)
print(list2_d)
#print(list2,list3)
#for c in list2:
 #   for d in list2:
 #       if c==d:
 #           list2.remove(d)
#for e in list2:
 #   for f in list3:
#        if e==f:
 #           list3.remove(f)
#print(list2,list3)