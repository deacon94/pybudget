class Category:

    def __init__(self, type):
        self.type = type
        self.category_amount = 0.00
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

    def transfer(source_category, amount, dest_category):
        # Initiate transfer
        if source_category.withdraw(amount, 'Transfer to ' + dest_category.type):
            # Only deposit if withdraw was successful           
            dest_category.deposit(amount, 'Transfer from ' + source_category.type)
            return True

        return False

    def get_balance(self):
        return self.category_amount

    def __str__(self):
        # Category Name
        string_output = self.type.center(30, '*') + '\n'

        # Ledger Items
        for ledger_entry in self.ledger:
            # Item description
            next_line = ledger_entry.get('description')[:23].ljust(23)

            # Item amount
            next_line = next_line + str(format(ledger_entry.get('amount'), '.2f')).rjust(7) + '\n'

            string_output = string_output + next_line
    
        # Category Total
        string_output = string_output + 'Total: ' + str(self.get_balance())

        return string_output
        
def create_spend_chart(categories):
    return 'TO DO'