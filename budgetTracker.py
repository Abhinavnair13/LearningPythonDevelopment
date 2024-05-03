import json
import random


def add_expense(initial_budget, expense):
    amount = float(input("Enter cost"))
    if initial_budget>amount:
        description = input("Enter description")
        expense.append({"description": description,"amount": amount})
        initial_budget-=amount
        print(f"Added expence {amount}, description : {description}\n Remaning budget {initial_budget}")
        return  initial_budget
    else:
        print("You dont have that much balance")
        print( random.Random(initial_budget))
        return initial_budget


def show_expense(expense, initial_budget):
    print(f"Remaning budget : {initial_budget}")
    for exp in expense:
        print(f'Cost : {exp["amount"]},description : {exp["description"]}')


def load_from_json(filepath):
    try:
        with open(filepath,'r') as file:
            data = json.load(file)
            return data["initial_budget"],data["expense"]
    except(FileNotFoundError,json.JSONDecodeError):
        return 0,[]




def save_into_json(filepath,initial_budget, expense):
    data ={
        "initial_budget": initial_budget,
        "expense": expense

    }
    with open(filepath,'w') as file:
        json.dump(data,file,indent=4,)



def main():
    print("Welcome to budget app")
    filepath = "budget_tracker.json"
    initial_budget,expense = load_from_json(filepath)

    if(initial_budget == 0):
        initial_budget=float(input("Please enter your budget"))
        expense = []
    
    

    while True:
        print("1. Add expense")
        print("2. Show expense")
        print("3. Exit")
        choice = int(input("Enter your choice"))
        if choice==1:
            print("Add expense")
            initial_budget= add_expense(initial_budget,expense)
        elif choice==2:
            print("Show expense")
            show_expense(expense,initial_budget)
        elif choice==3:
            save_into_json(filepath,initial_budget,expense)
            print("Exiting from the budget tracker...")
            exit()

if __name__== "__main__":
    main()
