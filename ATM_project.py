class ATM:
    def __init__(self):
        # Initialize private variables
        self.__balance = 0
        self.__pin = "123"
        self.__attempts = 3
        self.menu()

    def menu(self):
        # Display the main menu to the user
        user_input = input("""What would you like to do!
                         1. Check balance
                         2. Withdraw balance
                         3. Deposit balance
                         4. Change pin
                         5. Exit
                         """)

        if user_input == "1":
            # If user chooses to check balance, call the check_balance method
            self.check_balance()
        elif user_input == "2":
            # If user chooses to withdraw, call the deposit method
            self.deposit()
        elif user_input == "3":
            # If user chooses to deposit, call the withdraw method
            self.withdraw()
        elif user_input == "4":
            # If user chooses to change PIN, call the change_pin method
            self.change_pin()
        elif user_input == "5":
            # If user chooses to exit, return from the function, ending the program
            return

    def check_balance(self):
        # Check balance functionality
        while True:
            user_input = input("Enter your PIN: ")
            if user_input == self.__pin:
                # If the PIN is correct, display the balance and return to the main menu
                print(f"Your balance is {self.__balance}")
                self.menu()
                break
            else:
                # If the PIN is incorrect, decrement attempts and display remaining attempts
                self.__attempts -= 1
                print(f"Invalid PIN. {self.__attempts} attempts remaining.")

            if self.__attempts == 0:
                # If the maximum attempts are reached, inform the user and return to the main menu
                print("You have exceeded the maximum number of attempts. Returning.")

    def deposit(self):
        # Deposit functionality
        while True:
            user_input = input("Enter your PIN: ")
            if user_input == self.__pin:
                # If the PIN is correct, prompt for deposit amount and update the balance
                user_input = int(input("Enter your amount: "))
                self.__balance += user_input
                print("Deposit successful!")
                # Return to the main menu
                self.menu()
                break
            else:
                # If the PIN is incorrect, decrement attempts and display remaining attempts
                self.__attempts -= 1
                print(f"Invalid PIN. {self.__attempts} attempts remaining.")

            if self.__attempts == 0:
                # If the maximum attempts are reached, inform the user and return to the main menu
                print("You have exceeded the maximum number of attempts. Returning.")

    def withdraw(self):
        # Withdraw functionality
        while True:
            user_input = int(input("Enter your PIN: "))
            if user_input == self.__pin:
                # If the PIN is correct, prompt for withdrawal amount and update the balance
                user_input = int(input("Enter your amount: "))
                if user_input <= self.__balance:
                    self.__balance -= user_input
                    print("Withdrawal successful!")
                else:
                    # If the withdrawal amount exceeds the balance, inform the user
                    print("Insufficient balance")
                # Return to the main menu
                self.menu()
                break
            else:
                # If the PIN is incorrect, decrement attempts and display remaining attempts
                self.__attempts -= 1
                print(f"Invalid PIN. {self.__attempts} attempts remaining.")

            if self.__attempts == 0:
                # If the maximum attempts are reached, inform the user and return to the main menu
                print("You have exceeded the maximum number of attempts. Returning.")

    def change_pin(self):
        # Change PIN functionality
        while True:
            user_input = input("Enter your PIN: ")
            if user_input == self.__pin:
                # If the PIN is correct, prompt for a new PIN and update the PIN
                user_input = input("Enter your new PIN: ")
                self.__pin = user_input
                print("PIN changed successfully!")
                # Return to the main menu
                self.menu()
                break
            else:
                # If the PIN is incorrect, decrement attempts and display remaining attempts
                self.__attempts -= 1
                print(f"Invalid PIN. {self.__attempts} attempts remaining.")

            if self.__attempts == 0:
                # If the maximum attempts are reached, inform the user and return to the main menu
                print("You have exceeded the maximum number of attempts. Returning.")

# Create an instance of the ATM class
obj = ATM()
