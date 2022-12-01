class Category:
    amount = 0

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self,amount):
        print ("This is a deposit method:")
        self.amount += amount
        print("your have successfully deposited {} in {} category".format(amount, self.category))
        self.check_balance()
        return
    def check_balance(self):
        return "This is the current balance : {} ".format(self.amount)

    def withdraw(self):
        amount=input("How much would you like to withdraw:?\n")
        if (amount > self.amount):
            self.amount -= amount
        else:
            print("can't withdraw: low balance")
        return

    def transfer(self):
        return ("This is transfer method")



clothing_category = Category("clothing", 1000)
food_category =Category("food", 2000)
entertainment_category = Category("Entertainment", 500)
carexpense_category = Category("CarExpenses", 3000)
education_category =Category("Education", 2500)

print(clothing_category.deposit(1000))

#print(type(Budget))
#print(type(category_1))
