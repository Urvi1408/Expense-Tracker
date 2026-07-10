import csv

def next_id():

    expense_id = 1

    with open("data/expenses.csv", "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if not row:     
                continue
            expense_id = int(row[0]) + 1
    return expense_id

def addexpenses(d,c,des,a,p):

    expense_id=next_id()

    with open ("data/expenses.csv","a",newline="") as f :

        writer=csv.writer(f)
        writer.writerow([expense_id,d,c,des,a,p])

    print("Expense added successfully.")


def view_expenses():
    expenses=[]
    with open ("data/expenses.csv","r") as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:

            expenses.append({
                "expense_id": row[0],
                "date": row[1],
                "category": row[2],
                "description": row[3],
                "amount": row[4],
                "mode_of_payment": row[5]
            })

    return expenses 


def search_expenses(choice, search):

    expenses=[]
    with open("data/expenses.csv","r") as f:
        reader=csv.reader(f)
        next(reader)
        
        search=search.strip().lower()

        for row in reader:
            if choice==1 and search in row[1].lower():
                expenses.append({
                    "expense_id": row[0],
                    "date": row[1],
                    "category": row[2],
                    "description": row[3],
                    "amount": row[4],
                    "mode_of_payment": row[5]
                })

            elif choice == 2 and search in row[2].strip().lower():

                expenses.append({
                    "expense_id": row[0],
                    "date": row[1],
                    "category": row[2],
                    "description": row[3],
                    "amount": row[4],
                    "mode_of_payment": row[5]
                })

            elif choice == 3 and search in row[3].lower():

                expenses.append({
                    "expense_id": row[0],
                    "date": row[1],
                    "category": row[2],
                    "description": row[3],
                    "amount": row[4],
                    "mode_of_payment": row[5]
                })

            elif choice == 4 and search in row[5].lower():

                expenses.append({
                    "expense_id": row[0],
                    "date": row[1],
                    "category": row[2],
                    "description": row[3],
                    "amount": row[4],
                    "mode_of_payment": row[5]
                })

    return expenses


def change_expenses(expense_id,choice,new_value):
    with open ("data/expenses.csv","r",newline="") as f:
        reader=csv.reader(f)
    
        header=next(reader)
        rows=[]
        rows.append(header)
        found=False
        s=expense_id
        c=choice
        for row in reader:
            if row[0]==s:
                found=True
                ch=new_value
                if c==1:
                    row[1]=ch
                elif c==2:
                    row[2]=ch
                elif c==3 :
                    row[3]=ch
                elif c==4 :
                    row[4]=float(ch)
                elif c==5 :
                    row[5]=ch
            rows.append(row)
            

    with open ("data/expenses.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(rows)



def delete_expense(expense_id):
    with open ("data/expenses.csv","r") as f:
        reader=csv.reader(f)
        rows=[]
        s=expense_id
        header=next(reader)
        rows.append(header)
        found=False
        for row in reader:
            if row[0]==s:
                found=True
            else:
                rows.append(row)
                continue
        
    with open("data/expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
