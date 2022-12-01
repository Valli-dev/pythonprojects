import random
import datetime

## Initialze the system


userDatabase={1111111111: ['Seyi','Onifade','seyionifade@zuriteam.com', 'PasswordSeyi',1000],
              2222222222:["Mike", "Koss", "mikekoss@zuriteam.com", "PasswordMike",1500],
              3333333333:["Valli","mayil","vallimayil@gmail.com","PasswordMayil",1200]}



def init():

        print("******************* WELCOME TO BANK PHP **********************")
    #while(op = False):
        haveaccount= int(input("Do you have account with us? 1 (Yes) 2 (No) 3(exit)\n"))
        if (haveaccount == 1):
            login()
        elif(haveaccount ==2):
            register()
        elif(haveaccount==3):
            exit()
        else:
            print("please enter a valid option")
            init()


#register
  # input username , email, password

  # generate accountnumber

def register():
    print("********* New Account opening Registration: ********** \n")
    
    firstName = input("Enter your first name: \n")
    lastName = input("Enter your Last name: \n")
    email = input("Enter your email address: \n")
    password = input("Please create your password:\n")
    accountNumber = generateAccountNumber()
    
    userDatabase[accountNumber]=[firstName, lastName, email, password]
    #print("\n" , userDatabase.items())
    
    print("\nYour Account has been created successfully")

    print("**************Login details********************\n")
    print("Your account number is ",accountNumber)
    print("Make sure to keep it safe\n")
    print("************************************************\n")

    choice= input("Would you like to login to your account?(y/n)\n")
    if(choice=='y'): login()
    else: init()


#login
#(username or email) , password
# go to bank operations

def login():
    
    flag=0
    x= datetime.datetime.now()

    accountNumberFromUser = int(input("\nWhat is your Account Number?\n"))
    password = input("\nWhat is your password?\n")

    for accountNumber,userDetails in userDatabase.items():
        if (accountNumber==accountNumberFromUser and userDetails[3]==password) :               
            flag=1
            print("**************Login successful*************** @ " , x)
            bankOperation(userDetails)
    
    
    if (flag==0):
        print("Invalid account or password")
        op=input("Would you like to continue y/n?\n")
        if (op=='y'): login()
        else: 
            print("Quit\n")
            exit()




#bank operations

def bankOperation(user):

        print("************** Welcome %s %s ****************\n" %(user[0], user[1]))
    
        selectedOption= int(input(" What would you like to do?\n Bank operations:\n 1. Withdrawal\n 2. Cash Deposit\n 3. logout Account \n 4. Exit Bank operations\n "))
    #while(selectedOption !=4):

        if (selectedOption == 1):
            print("\nWithdrawal function")
            withdrawOperation()
            op=input("would you like another operation(y/n)")
            if (op=='y'):
                bankOperation(user)
            else:
                exit()
   
        elif(selectedOption == 2):
            print("\nDeposit function")
            depositOperation()
            op=input("would you like another operation(y/n)")
            if (op=='y'):
                bankOperation(user)
            else:
                exit()
            

        elif(selectedOption == 3):
            print("Logging OUT of your account!")
            init()

        elif (selectedOption ==4):
            print("Quit Bank Operations\n")
            exit()
        else:
            print("Invalid option")
            bankOperation( user)



    





def withdrawOperation():
    Amount= int(input("How much do you want to withdraw?\n"))
    print("Take your cash!!!")
    

    

def depositOperation():
    Amount= int(input("How much do you want to deposit?\n"))
    print("cash deposited!!!")



def generateAccountNumber():
    print("Generating Account Number")
    return random.randrange(1111111111,9999999999)
    

####ACTUAL BANKING SYSTEM######

init()



