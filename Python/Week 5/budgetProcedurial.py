funds = 2500
budgets ={}
expenses ={}
def Addbudget(name, amount):
      global funds
      if name is budgets:
            raise ValueError("Budget for item already exists")
      if amount > funds:
        raise ValueError("No can do you are too broke")
      budgets[name] = amount 
      funds = funds - amount
      expenses[name] = 0
      return funds 

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("Item not in budget")
    expenses[name] += amount
    budgeted = budgets[name]
    spent =  expenses[name]
    return budgeted - spent
    
def PrintBudgeted():
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        return budgeted - spent
    
    
def PrintBudgeted():
    print("Budget             Budgeted    Spent.  Remaining")
    print("-----------------------------------------------")
    totalBudgeted = 0
    totalspent = 0
    totalremaining = 0
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingBudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}'
        , f'{remainingBudget:10.2f}')
        totalBudgeted += budgeted
        totalspent += spent
        totalremaining = remainingBudget
     print(f'{"Total":15s}, {totalBudgeted:10.2f}, {totalspent:10.2f}'
        , f'{totalBudgeted- totalspent:10.2f}')


print("Total Funds:",funds)
Addbudget("Books",100)
Addbudget("Rent", 800)
Addbudget("Car Note", 200)


Spend("Books", 50)
Spend("Rent", 800)
Spend("Car Note", 200)

PrintBudgeted()
