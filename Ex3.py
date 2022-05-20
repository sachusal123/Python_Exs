i=1
s=0
for i in range(21):
    if i%2!=0 and i%3!=0:
        print(i)
        s=s+i
    i=i+1
print("Sum=",s)