class Budget:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self):
        while True:
            try:
                deposit_amount = float(input('How much would you like to deposit? '))
            except ValueError:
                print('Invalid input, try again')
            else:
                break

        self.balance += deposit_amount
        print('Cash deposited successfully')

    def withdraw(self):
        while True:
            try:
                withrawal_amount = int(input('How much would you like to withdraw? '))
            except ValueError:
                print('Invalid input, try again')
            else:
                break
        if self.balance == 0 or self.balance < withrawal_amount:
            print('Insufficient fund')
        else:
            self.balance -= withrawal_amount
            print(f'£{withrawal_amount} cash succesfully withdrawn')
            print('Take your cash!')


def option_input():
    while True:
        try:
            option = int(input('Please select an option from the above(Must be a number): '))
        except ValueError:
            print('invalid input, try again')
        else:
            break
    return option


print('Hello, hope your day is going well!')
while True:
    print()
    print('1. Operate on Food Budget')
    print('2. Operate on Clothing Budget')
    print('3. Operate on Entertainment Budget')
    print('4. Quit')
    print()
    option = option_input()

    if option == 1:
        food = Budget()
        food.deposit()
        print(f'You current balance is: £{food.balance}')
        print()
        food.withdraw()
        print(f'You current balance is: £{food.balance}')

    elif option == 2:
        clothing = Budget(balance=food.balance)
        clothing.deposit()
        print(f'You current balance is: £{clothing.balance}')
        print()
        clothing.withdraw()
        print(f'You current balance is: £{clothing.balance}')

    elif option == 3:
        entertaiment = Budget(balance=clothing.balance)
        entertaiment.deposit()
        print(f'You current balance is: £{entertaiment.balance}')
        print()
        entertaiment.withdraw()
        print(f'You current balance is: £{entertaiment.balance}')

    elif option == 4:
        break
