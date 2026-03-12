# INT240106710 Ayberk Yahşi

balance = 100.50
pin = 4567
is_active = True
bloke = 3


while bloke > 0:
    girilen_sifre = int(input(f"Please enter your PIN (Attempts left: {bloke}): "))

    if girilen_sifre == pin:
        print("\nCorrect PIN")
        print("Welcome, User")
        is_active = True
        break

    else:
        bloke -= 1
        if bloke > 0:
            print("Incorrect PIN try again")
        else:
            print("You entered the wrong information 3 times, blocked")
        is_active = False


while is_active:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    secim = int(input("Enter your choice: "))

    if secim == 1:
        print(f"Your current balance is {balance:.2f}")

    elif secim == 2:
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print(f"{deposit} $ Successfully deposited. New balance: {balance:.2f}")

    elif secim == 3:
        withdraw = float(input("Enter amount to deposit: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"{withdraw} $ Successfully withdrew. New balance: {balance}")
        else: 
            print("Insufficient amount")

    elif secim == 4:
        print("Thank you for using ATM")
        is_active = False

    else:
        print("Invalid keypad")


    






