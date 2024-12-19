from operator import truediv


def your_balance():
    print("Your balance is Rs",balance)

def deposit():
    amount=float(input("enter the amount to be deposited"))
    if amount<0:
        print("it is not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("enter the amount to be withdrawn"))
    if amount>balance:
        print("insufficiant balcnce")
        return 0
    elif amount<0:
        print("insufficiant amount")
        return 0
    else:
        return amount
balance=0
run=True

while run:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4):")

    if choice == '1':
        your_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("That is not a valid choice")

















































































































