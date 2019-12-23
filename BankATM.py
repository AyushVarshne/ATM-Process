print("Welcome to Axis Bank ATM")
restart=("Y")
chances=3
balance=0.00
while chances>=3:
    pin=int(input("Please enter your 4 digit pin:"))
    if pin==(1234):
        print("Your entered pin is correct\n")
        while restart not in('n','No','no','N'):
            print('Please press1 for your Balance\n')
            print('Please press 2 to make a widrawl\n')
            print('Please press 3 to Pay in\n')
            print('Please press 4 to return card\n')
            option=int(input("What would you like to choose"))
            if option==1:
                print("Your balance is",balance,'\n')
                restart=input('Would you like to go back')
                if restart not in('n','No','no','N'):
                    print('Thank you')
                    break
            elif option==2:
                option2=('Y')
                withdrawl=int(input("How Much You want to withdrawl the money"))
                if withdrawl in [10,20,40,60,80,100]:
                    balance=balance-withdrawl
                    print('\n your balance is now',balance)
                    restart=input('Would you like to go back?')
                    if restart in ('n','No','N','no'):
                        print('Thank You')
                        break
                elif withdrawl!=[10,20,40,60,80,100]:
                    print('Invalid Amount,Please re-try\n')
                    restart=('Y')
                elif withdrawl==1:
                    withdrawl=int(input("Please enter desired amount:"))
            elif option==3:
                pay_in=int(input("How much would you like to pay in"))
                balance=balance+pay_in
                print('/n Your balance is now',balance)
                restart=input("Would you like to go back?")
                if restart in ('n','No','no','N'):
                    print("Thank You")
            elif option==4:
                print('Please wait while your card is return..... \n')
                print("Thank You for your service")
                break
            else:
                print('please enter a correct no.\n')
                restart=('Y')
    elif pin !=('1234'):
        print('Incorrect Passoword')
        chances=chances-1
        if chances==0:
            print('\n No more tries')
            break
