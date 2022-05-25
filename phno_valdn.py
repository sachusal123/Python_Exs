import re
n=input("Enter phone number:")
# 1) first dig contain nos bw 6 to 9
    # 2) Then the rest 9 dig contain nos 0-9
    # 3) Then contains 9 digits
Pattern = re.compile("(0|91)?[6-9][10-9]{9}")
a= Pattern.match(n)
if a:
    print("its a phone no")
else:
    print("not a phone no")