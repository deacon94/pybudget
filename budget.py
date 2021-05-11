class Category:

    def __init__(self, type):
        self.type = type
        self.category_amount = 0.00
        self.total_withdraw = 0.00
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
            self.total_withdraw += amount

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
    total = 0

    return_chart = 'Percentage spent by category\n'

    # Compute total
    for cat in categories:
        total += cat.total_withdraw

    # Loop by 
    for i in range(100, -1, -10):
        next_line = str(i).rjust(3) + '|'

        for cat in categories:
            if i <= ((cat.total_withdraw/total)*100) - (((cat.total_withdraw/total)*100)%10):
                # Add to current line
                next_line = next_line + ' o ' 
            else:
                next_line = next_line + '   '

        # Add latest line to return string
        return_chart = return_chart + next_line + ' \n'

    return_chart = return_chart + '    ' + str('-').center(((len(categories)*3)), '-') + '-\n'

    # Loop through each category name
    max_height = 0
    i = 0

    # Figure out the longest category name
    for cat in categories:
        max_height = max(max_height, len(cat.type))

    # Loop by longest (vertically), then across by category
    for i in range(0, max_height):
        next_line = '    '

        for cat in categories:
            if i < len(cat.type):
                # Add to current line
                next_line = next_line + ' ' + cat.type[i] + ' '
            else:
                next_line = next_line + '   '

        # Add latest line to return string
        if i < max_height - 1:
            return_chart = return_chart + next_line + ' \n'
        else:    
            return_chart = return_chart + next_line + ' '

    return return_chart