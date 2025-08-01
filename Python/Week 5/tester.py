import budget

myBudget = budget.BudgetManager(2500)
print("Total Funds:", myBudget.funds)
myBudget.Addbudget("Books",100)
myBudget.Addbudget("Rent", 800)
myBudget.Addbudget("Car Note", 200)


myBudget.Spend("Books", 50)
myBudget.Spend("Rent", 800)
myBudget.Spend("Car Note", 200)

myBudget.PrintBudget()
