# # personal expense tracker project
# import tkinter as tk
# from tkinter import messagebox
# expenses=[]
# def add_expense():
#     date=entry_date.get()
#     category=entry_category.get()
#     amount=entry_amount.get()
#     if not date or not category or not amount:
#         messagebox.showerror("error","all feilds are required")
#         return
#     expenses.append({
#         "date":date,
#         "category":category,
#         "amount":float(amount)
#     })
#     messagebox.showinfo("success","expense added")
#     clear_feild()
# def view_expenses():
#     output.delete(1.0,tk.END)
#     for exp in expenses:
#         output.insert(tk.END,f"{exp['date']} | {exp['category']} | {exp['amount']}\n")
# def total_expenses():
#     total=sum(exp['amount'] for exp in expenses)
#     messagebox.showinfo("Total",f"total expenses:{total}")
# def category_total():
#     if not expenses:
#         messagebox.showinfo("Info","no expense  available")
#         return
#     summary={}
#     for exp in expenses:
#         category=exp['category']
#         if category in summary:
#             summary[category] +=exp['amount']
#         else:
#             summary[category]=exp['amount']
#     output.delete(1.0,tk.END)
#     for c,total in summary.items():
#         output.insert(tk.END,f"{c}:{total}\n")
# def clear_feild():
#     entry_amount.delete(0,tk.END)
#     entry_date.delete(0,tk.END)
#     entry_category.delete(0,tk.END)
# # gui window
# root=tk.Tk()
# root.title("Expense Tracker")
# tk.Label(root,text="Date").grid(row=0,column=0)
# entry_date=tk.Entry(root)
# entry_date.grid(row=0,column=1)
# tk.Label(root,text="Category").grid(row=1,column=0)
# entry_category=tk.Entry(root)
# entry_category.grid(row=1,column=1)
# tk.Label(root,text="Amount").grid(row=2,column=0)
# entry_amount=tk.Entry(root)
# entry_amount.grid(row=2,column=1)
# tk.Button(root,text="Add Expense",command=add_expense).grid(row=3,column=0)
# tk.Button(root,text="View Expenses",command=view_expenses).grid(row=3,column=1)
# tk.Button(root,text="Total Expenses",command=total_expenses).grid(row=4,column=0)
# tk.Button(root,text="Category Expenses",command=category_total).grid(row=4,column=1)
# output=tk.Text(root,height=10,width=40)
# output.grid(row=5,column=0,columnspan=2)
# root.mainloop()
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
