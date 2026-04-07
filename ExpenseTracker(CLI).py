expense_list=[]
#  function 1 adding expenses(date,category,amount)
def add_expense():
    date=input("Enter the Date (dd-mm-yyyy)")
    category=input("Enter the category(food,travel,fee,shopping,other)")
    amount=float(input("Enter the amount"))
    expense={'Date':date,'Category':category,'Amount':amount}
    expense_list.append(expense)
    print("data is added sucessfully")
# function 2 view expenses
def view_expenses():
    if not expense_list:
        print('\n no data avialable')
        return
    for exp in expense_list:
        print(f"Date:{exp['Date']},Catagory:{exp['Category']},Amount:{exp['Amount']}")
# function 3 calculate total expenses and print
def total_expenses():
    if not expense_list:
        print('\n no data available')
        return
    total_expenses=0
    for exp in expense_list:
        total_expenses=total_expenses+exp['Amount']
    print('\n Total Expenses:',total_expenses)
# function 4 for caregory wise total
def category_total():
    cat=set()
    for exp in expense_list:
        cat.add(exp['Category'])
    for c in cat:
        category_total=0
        for exp in expense_list:
            if exp['Category']==c:
                category_total=category_total+exp['Amount']
        print(f'{c}:{category_total}')
# main fuction
def main():
    while(True):
        print('#personal Expense Tracker#')
        print('1.add expense')
        print('2.view expenses')
        print('3.total expenses')
        print('4.category wise expenses')
        choice=input("enter choice")
        print('5.Exit')
        if choice=='1':
            add_expense()
        if choice=='2':
            view_expenses()
        if choice=='3':
            total_expenses()
        if choice=='4':
            category_total()
        elif choice=='5':
            print('exit')
            break
        else:
            print('give proper choice')
main()