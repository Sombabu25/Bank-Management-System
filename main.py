class Bank:

    Bank_Name="Canara Bank"
    Bank_address="Surampalem"

    # value initialization
    def __init__(self,name,pan,address):
        self.name=name
        self.pan=pan
        self.address=address
        self.balance=0


    # display user information
    def show_info(self):
        print(f"{self.name} your account created successfuly")

   # deposite method
    def deposit(self):
        amount=int(input("enter amount to deposit:"))
        self.balance += amount
        print(f"{amount} deposited successfully")

    # withdrawn method
    def withdraw(self):
        amount=int(input("enter amount to withdraw:"))

        if self.balance > amount:
           self.balance -= amount
           print(f"\n {amount} withdrawn successfuly")

        else:
            print("insufficient amount")

    # mini statement
    def statement(self):
        print(f"account balance is:{self.balance}")


# get user information
print(f"Welcome to {Bank.Bank_Name} at {Bank.Bank_address}")
name=input("enter your name:")
pan_number=input("enter your pan number:")
address=input("enter your address:")
print()


obj=Bank(name,pan_number,address)
obj.show_info()
print()


while True:
    print("choose an option:")
    choice=input("1.deposit\n2.withdraw\n3.mini statement\n4.exit\n")

    if choice == "1":
       obj.deposit()

    if choice == "2":
       obj.withdraw()

    if choice == "3":
       obj.statement()

    if choice == "4":
       break


print("Thanks for visiting !!!!")














