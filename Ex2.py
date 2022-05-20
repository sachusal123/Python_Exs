emp_id=input("Enter employee ID::")
emp_name=input("Enter employee Name::")
basic_pay=int(input("Enter Basic Pay::"))

if basic_pay>10000:
   hra=basic_pay*0.15
   da=basic_pay*0.08
   net_pay=basic_pay+hra+da
   
elif basic_pay>5000 and basic_pay<1000:
   hra=basic_pay*0.1
   da=basic_pay*0.05
   net_pay=basic_pay+hra+da
   
elif basic_pay<5000:
   hra=basic_pay*0.05
   da=basic_pay*0.03
   net_pay=basic_pay+hra+da
else :
    print("Invalid")
 
print("Basic pay of",emp_name,"(",emp_id,") =",basic_pay)  
print("HRA of",emp_name,"(",emp_id,") =",hra) 
print("DA of",emp_name,"(",emp_id,") =",da)
print("net_pay of",emp_name,"(",emp_id,") =",net_pay)

