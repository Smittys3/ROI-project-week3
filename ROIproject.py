# monthly income
# expenses
# monthly cashflow = income - expenses
# ROI% = annual cash flow/total investment
# total investment = down payment + closing cost + rehab budget + misc other


class ROI:
    def __init__(self, property = 0):
        self.property = property

    def mn_income(self):
        self.property = int(input("What is your monthly income?: "))
        self.monthly_income = int(self.property)
        print(f" Your monthly income is {str(self.monthly_income)}")

    def exp(self):
        expenses = int(input("What is your monthly expenses?:  "))
        self.expenses = int(expenses)

    def cashflow(self):
        self.monthly_cashflow = int(self.monthly_income) - int(self.expenses)
        print(f"Your total monthly cash flow is {int(self.monthly_income) - int(self.expenses)}")

    def cal_roi(self):
        annual_cashflow = int(self.monthly_cashflow) * 12
        print(f"Your annual cashflow {annual_cashflow}")
        total_investment = int(input("What is your total investment?:  "))
        return f"Your ROI (return of investment) is {float((annual_cashflow / total_investment) * 100)} percent"

apartment = ROI()
print(apartment.mn_income())
print(apartment.exp())
print(apartment.cashflow())
print(apartment.cal_roi())
