n=input("Enter an String:")
import re
x = re.sub("\s","_",n)
y=re.sub("_"," ",x)
print(x)
print(y)