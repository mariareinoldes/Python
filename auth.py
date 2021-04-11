import random
#Creating a bank account

database = {} #dictionary

def init():

    print('***** Welcome to Python Bank *****')

    haveAccount = int(input('Do you have an account with us? \n1 - YES \n2 - NO\n'))
    if (haveAccount == 1):
        login()
    elif (haveAccount == 2):
        print(register())
    else:
        print('You have selected an invalid option')
        init()

def login():

    print('\n***** LOGIN *****\n')

    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
    print('Invalid account or password\n')

    login()
    

def register():

    print('\n***** REGISTER *****\n')

    email = input('What is your email address?\n')
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')
    password = input('Create a password for yourself\n')

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]
    # colecting all the datas from the user and stocking in a list
    
    print('***** Your account has been created *****\n')
    print('Your account number is: %s\n' % accountNumber)
    login()

def bankOperation(user):

    print('\nWelcome %s %s\n' % (user[0], user[1]))

    selectedOption = int(input('What yould you like to do? \n 1 - Deposit\n 2 - Withdrawal\n 3 - Logout\n 4 - Exit\n'))

    if(selectedOption == 1):
        depositOperation(user)

    elif(selectedOption == 2):
        withdrawalOperation(user)

    elif(selectedOption == 3):
        login()

    elif(selectedOption == 4):
        exit()

    else:
        print('Invalid option selected, please try again')
        bankOperation(user)

def withdrawalOperation(user):
    print('\n***** Withdrawal *****\n')
    valueWithdraw = float(input('How much would you like to withdraw? \n'))
    print(f'You are withdrawing {valueWithdraw}, please take your money.\n')
    bankOperation(user)

def depositOperation(user):
    print('\n***** Deposit Operations *****\n')
    valueDeposit = float(input('How much would you like to deposit? \n'))
    print(f'Your deposit was of $ {valueDeposit}\n')
    bankOperation(user)

def generationAccountNumber():
    print('Generating Account Number')
    return random.randrange(1111111111,9999999999)

def logout():
    login()

init()