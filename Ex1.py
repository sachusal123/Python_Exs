a= []
s=0
for i in range(6):
    it=int(input("Enter the mark of subject\t"))
    s=s+it
    a.append(it)
avg=s//6
print("Average=",avg)
if avg>90:
    print("A Grade")
elif avg>80:
    print("b Grade")
elif avg>70:
    print("C Grade")
elif avg>60:
    print("D Grade")
elif avg>50 :
    print("E Grade")
elif avg<40:
    print("Failed")
else:
    print("Failed")