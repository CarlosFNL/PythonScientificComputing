class Category:
    def __init__(self,description):
        self.description = description
        self.ledger = []
        self.balance = 0.0
    
    def __str__(self):
        header = self.description.center(30,"*") + '\n'
        ledger = ''
        for item in self.ledger:
            line_description = "{:<23}".format(item['description'])
            line_amount = "{:>7.2f}".format(item['amount'])
            ledger += "{}{}\n".format(line_description[:23],line_amount[:7])
        total = "Total: {:.2f}".format(self.balance)
        return header + ledger + total

    def deposit(self,amount,description):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    def withdraw(self,amount,description=''):

        if (self.balance - amount) >= 0:
            self.ledger.append({'amount': -1*amount, 'description': description})
            self.balance -= amount
            return True
        
        else:
            return False
        
    def get_balance(self):
        return self.balance
    
    def transfer(self,amount,category_instance):
        if self.withdraw(amount, "Transfer to {}".format(category_instance.description)):
            category_instance.deposit(amount, "Transfer from {}".format(self.description))
            return True
        else:
            return False

        
    def check_funds(self,amount):

        if amount > self.balance:
            return False
        else:
            return True

def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))