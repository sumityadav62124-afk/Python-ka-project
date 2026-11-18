print("===== WELCOME TO PYTHON ATM =====")

balance = 5000
pin = 1234

user_pin = int(input("Enter your ATM PIN: "))

if user_pin == pin:

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your Balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            balance = balance + amount
            print("Money Deposited Successfully!")
            print("New Balance:", balance)

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance = balance - amount
                print("Please Collect Your Cash")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank You for Using Python ATM!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN!")
