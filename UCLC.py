string_ul=input("Enter an String:")
i=len(string_ul)
j=0
upper_count=lower_count=0
while j<i:
    if string_ul[j].isupper():
        upper_count=upper_count+1
    else:
        lower_count=lower_count+1
    j=j+1
print("Number of upper cases in ",string_ul," is ",upper_count)
print("Number of lower cases in ",string_ul," is ",lower_count)