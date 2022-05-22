n=input("Enter an string::")
j=0
c=0
i=len(n)
while j<i:
   if n[j]== "a":
      c=c+1
   elif n[j]== "e":
      c=c+1
   elif n[j]== "i":
      c=c+1
   elif n[j]== "o":
      c=c+1
   elif n[j]== "u":
      c=c+1
   else:
      pass
   j=j+1
print("Total Number of vowels in ",n," is ",c)