
class Category:
    def __init__(self, category_name):          #Initial set up for the variables
        self.name = category_name
        self.ledger = []
        self.account_total = 0
        self.withdraw_total = 0
    def deposit(self, amount, description = ""):                #deposit and add what it was
        self.ledger.append({"amount": amount, "description": description})
        self.account_total += amount
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) is False:
            return False
        amount = amount * -1
        self.ledger.append({"amount": amount, "description": description})
        self.account_total += amount
        self.withdraw_total += amount
        return True
    def get_balance(self):
        return self.account_total
    def transfer(self, amount, category):
        if self.check_funds(amount) is False:
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True
    def check_funds(self, amount):
        if self.account_total < amount:
            return False
        return True
    def __str__(self):  # gives a string output when printed. Self is whatever the input category class is (like food or clothing) and

        # Section for making the ledger title
        budget_ledger = ""
        asterisk_N = ""
        if (len(self.name) % 2) != 0:
            return "Sorry, only even length words are implemented right now"

        asterisk_len = round(15 - (len(self.name)/2))
        for i_asterisk in range(0, asterisk_len):
            asterisk_N += '*'

        budget_ledger += asterisk_N + self.name + asterisk_N + '\n'



        # Section for making string for ledger items
        budget_ledger_list = []
        spaces_amount = "       "
        spaces_description = "                       "
        for i_ledger in self.ledger:

            # get description in a string 23 characters long
            description_string = i_ledger['description']
            description_len = len(description_string)
            if description_len >= 23:
                description_string = description_string[0:23]
            else:
                N_Spaces = 23 - description_len
                description_string += spaces_description[
                                      0:N_Spaces]  # create the string with spaces tacked onto the END

            # get the amount into a string 7
            amount_decimal = "{:.2f}".format(i_ledger["amount"])  # gets the amount from item list then makes it 2 decimal places
            amount_len = len(amount_decimal)
            if amount_len >= 7:
                amount_string = amount_decimal[0:7] + '\n'
            else:
                N_Spaces = 7 - amount_len
                amount_string = spaces_amount[0:N_Spaces] + str(amount_decimal) + '\n'  # create the string with spaces tacked onto the front

            budget_ledger += description_string + amount_string
            budget_ledger_list.append((description_string, amount_string))

        # Section for the total amount shown
        total_decimal = "{:.2f}".format(self.account_total)
        total_string =  "Total: " + total_decimal
        budget_ledger += total_string

        return budget_ledger



def create_spend_chart(categories):
    withdrawal_dict = {}
    grand_total_withdraw = 0
    chart = ""
    per_num = ['100', ' 90', ' 80', ' 70', ' 60', ' 50', ' 40', ' 30', ' 20', ' 10', '  0']
    for i_categories in categories:
        grand_total_withdraw += i_categories.withdraw_total

    # find the percentage of withdrawal
    for i_categories in categories:
        perc_withdrawal = i_categories.withdraw_total / grand_total_withdraw
        withdrawal_dict[i_categories.name] = withdrawal_dict.get(i_categories.name, perc_withdrawal)

    chart += "Percentage spent by category\n"
    for i_num in per_num:
        chart += i_num + "|"
        for ii_key, ii_val in withdrawal_dict.items():
            if ii_val >= int(i_num) / 100:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    chart += "    "

    longest_word = 0 #use this in the next session
    for i_categories in categories:
        for ii_dash in range(0,3):
            chart += "-"
        if len(i_categories.name) > longest_word:
            longest_word = len(i_categories.name)
    chart += "-\n"

    for i_lines in range(0, longest_word):
        chart += "    "
        for ii_key, ii_val in withdrawal_dict.items():
            if i_lines + 1 <= len(ii_key):
                chart += " " + ii_key[i_lines] + " "
            else:
                chart += "   "
        chart += " \n"
    chart = chart[0:-1]
    return chart



