y  = float(input('enter the total amount in the account'))
print(f"The Initial ammount is  {y} ")
x = float(input("Enter the amount to be withdraw in multiple of 5 :"))
print(x)
if x<=y:
    if x%5==0:
        remain_amount = 0
        remain_amount = y-x-x*0.50
        print(f"Remaining amount in account is :{remain_amount}")
        print(f"Charges for successful transactions are : {0.50}")
    else:
        
        print(f"Please Enter amount in multiple of 5 : {x} ")
        
else:
     print("Insufficient balance in your account")
  

