class Category:

    def __init__(self, type):
        self.type = type
        self.category_amount = 0
        self.ledger = list()

    def deposit(self, amount, description=''):
        # Add amount to category_amount
        if (amount > 0):
            self.category_amount = self.category_amount + amount 
            # self.ledger.append

# ledger = list of dictionary objects {"amount": amount, "description": description}

    def get_balance(self):
        return self.category_amount

def create_spend_chart(categories):
    return 'TO DO'