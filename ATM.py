Balance=5000
pin=1234

print("...............WELCOME TO ATM MACHINE.......")

user_pin=int(input("Enter your 4-digit pin:"))

if user_pin==pin:
    print("\n Login successful")

    print("\n2 Check balance")
    print("\n3 Withdraw Mony")
    print("\n4 Deposite Mony")
    print("\n5 Exist")

    choice=int(input("\nEnter your choice(1-4):"))
    if choice==1:
        print(f"\n Your current balance is:₹{Balance}")

    elif choice==2:
        amount=int(input("Enter Amount to withdraw:₹"))
        if amount<=Balance:
            Balance=Balance-amount
            print(f"\n Withdra successfull Remaining balance:₹{Balance}")
        else:
            print("\n insufficient balance")
    elif choice==3:
          amount=int(input("Enter Amount Deposite:₹ "))  
          Balance+=amount
          print(f"\n Deposite successefull ! New Balance:₹{Balance}")

    elif choice==4:
         print("\n Tank you for using ATM") 
    else:
        print("\n Invalid Choice")  
else:
    print("\n Incorrect Pin Pleas Try Again")
