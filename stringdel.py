string_ip=input("Enter an string::")
print("Actual String is : ","'",string_ip,"'")
string_del=input("Enter The word to delete from the above string:")
string_split=string_ip.split()
string_length=len(string_split)
i=0
j=0

for a in string_split:
    if a==string_del:
       j=1
       string_split.remove(a)

if(j==0):
    print(string_del, "is Not availible in the ",string_ip)

print("String after deletion::",string_split)
