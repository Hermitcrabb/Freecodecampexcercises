class Category:
    def __init__(self,name):
        self.name =name
        self.ledger = []
    
    def __str__(self):
        # Title
        title = f"{self.name:*^30}\n"

        # Items
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23].ljust(23)
            amount = f"{entry['amount']:.2f}"[:7].rjust(7)
            items += f"{description}{amount}\n"

        # Total
        total = f"Total: {self.get_balance():.2f}"

        return title + items + total
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount,'description': description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,'description': description})
            return True
        return False

    def get_balance(self):
        total = sum(item['amount'] for item in self.ledger)
        return total
    
    def transfer(self,amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self,amount):
        return amount <= self.get_balance()
        

def create_spend_chart(categories):
    # Step 1: Spending per category
    spent = [sum(-item['amount'] for item in cat.ledger if item['amount'] < 0) for cat in categories]
    total = sum(spent)

    # Step 2: Percentages floored to nearest 10
    percents = [int((s / total) * 100) // 10 * 10 if total else 0 for s in spent]

    # Step 3: Chart lines
    chart_lines = []
    for level in range(100, -1, -10):
        line = f"{level:>3}| "
        for p in percents:
            line += "o  " if p >= level else "   "
        chart_lines.append(line)

    # Step 4: Divider line - exactly 3 dashes per category + 1 at the end
    divider = "    " + "-" * (len(categories) * 3 + 1)

    # Step 5: Vertical names - FIXED: Ensure every line has exactly the same length
    names = [c.name for c in categories]
    max_len = max(len(n) for n in names)
    name_lines = []

    for i in range(max_len):
        line = "     "  # 5 spaces at the start
        for n in names:
            if i < len(n):
                line += n[i] + "  "  # character + 2 spaces
            else:
                line += "   "  # space + 2 spaces = 3 characters total
        # Remove the trailing 2 spaces from the last category
        line = line.rstrip()
        # Add the required 2 spaces after the final category
        line += "  "
        name_lines.append(line)

    # Step 6: Combine everything
    result = "Percentage spent by category\n"
    result += "\n".join(chart_lines) + "\n"
    result += divider + "\n"
    result += "\n".join(name_lines)
    
    return result




food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
food.transfer(50, clothing)
clothing.withdraw(25.55, "shirt")
entertainment.withdraw(30, "movie night")

print(food)

print(create_spend_chart([food, clothing, entertainment]))
