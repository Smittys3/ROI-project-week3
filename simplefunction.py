# monthly income
# expenses
# monthly cashflow = income - expenses
# ROI% = annual cash flow/total investment
# total investment = down payment + closing cost + rehab budget + misc other


monthly_income = 2000
expenses = 1610
total_investment = 50000

# # # # Function for finding the ROI
def ROI(monthly_income, expenses):
    monthly_cashflow = (monthly_income - expenses)
    annual_cashflow = monthly_cashflow * 12
    ROI = ((annual_cashflow / total_investment) * 100)
    print(ROI)

ROI(monthly_income, expenses)