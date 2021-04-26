class Category:

    def __init__(self, type):
        self.type = type
        self.category_amount = 0
        self.ledger = list()

    def deposit(self, amount, description=''):
        if (amount > 0):
            # Add amount to category_amount (for easy calculations)
            self.category_amount = self.category_amount + amount 

            # Adjust ledger
            self.ledger.append({'amount': amount, 'description': description})

    def check_funds(self, amount):
        # Check to see if the amount can be removed (enough $ exists to cover)
        if (self.category_amount >= amount):
            return True
        else:
            return False

    def withdraw(self, amount, description=''):
        # Confirm there are enough funds to make withdraw
        if (amount > 0) and (self.check_funds(amount)):
            # Subtract amount to category_amount (for easy calculations)
            self.category_amount = self.category_amount - amount 

            # Adjust ledger
            neg_amount = amount * -1
            self.ledger.append({'amount': neg_amount, 'description': description})

            return True

        # Not enough funds
        return False

    def transfer(self, amount, dest_category):
        


    def get_balance(self):
        return self.category_amount

def create_spend_chart(categories):
    return 'TO DO'