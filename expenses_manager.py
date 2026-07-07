import csv

def next_id():
    with open("expenses.csv","r",newline="") as f:
        expense_id=1
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            expense_id=int(row[0])+1
        
    return expense_id

def addexpenses():

    expense_id=next_id()
    d=input("Enter date(dd-mm-yyyy):")
    c=input("Enter Category:")
    des=input("Enter description:")
    a=float(input("Enter amount:"))
    p=input("enter mode of payment")

    with open ("expenses.csv","a",newline="") as f :

        writer=csv.writer(f)
        writer.writerow([expense_id,d,c,des,a,p])

    print("Expense added successfully.")


def view_expenses():

    with open ("expenses.csv","r") as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            print(f"""
                    ID: {row[0]}
                    Date: {row[1]}
                    Category: {row[2]}  
                    Description: {row[3]}
                    Amount: ₹{row[4]}
                    Payment: {row[5]}
                """)


def search_expenses():

    with open("expenses.csv","r") as f:
        reader=csv.reader(f)
        
        print("""
                Search By:
                1. Date
                2. Category
                3. Description
                4. Payment Mode
            """)

        c=int(input("Enter your choice:"))
        s=input("Enter what u want to search:")

        next(reader)
        found=False

        for row in reader:
            if (c==1) and (row[1].lower()==s.lower()):
                print(f"""
                    ID: {row[0]}
                    Date: {row[1]}
                    Category: {row[2]}  
                    Description: {row[3]}
                    Amount: ₹{row[4]}
                    Payment: {row[5]}
                """)
                found=True
            elif (c==2) and (row[2].lower()==s.lower()):
                print(f"""
                    ID: {row[0]}
                    Date: {row[1]}
                    Category: {row[2]}  
                    Description: {row[3]}
                    Amount: ₹{row[4]}
                    Payment: {row[5]}
                """)
                found=True
            elif(c==3) and (row[3].lower()==s.lower()):
                print(f"""
                    ID: {row[0]}
                    Date: {row[1]}
                    Category: {row[2]}  
                    Description: {row[3]}
                    Amount: ₹{row[4]}
                    Payment: {row[5]}
                """)
                found=True
            elif(c==4) and (row[5].lower()==s.lower()):
                print(f"""
                    ID: {row[0]}
                    Date: {row[1]}
                    Category: {row[2]}  
                    Description: {row[3]}
                    Amount: ₹{row[4]}
                    Payment: {row[5]}
                """)
                found=True
            else:
                continue
        
        if found==False:
            print("No matching expense found.")


def change_expenses():
    with open ("expenses.csv","r",newline="") as f:
        reader=csv.reader(f)

        print("Select the field you want to change:")
        print("1. Date")
        print("2. Category")
        print("3. Description")
        print("4. Amount")
        print("5. Payment Mode")

        c=int(input("Enter your choice:"))
        s=input("Enter expense id:")
        found=False
        header=next(reader)
        rows=[]
        rows.append(header)

        for row in reader:
            if row[0]==s:
                found=True
                ch=input("Enter the new value:")

                if c==1:
                    row[1]=ch
                elif c==2:
                    row[2]=ch
                elif c==3 :
                    row[3]=ch
                elif c==4 :
                    row[4]=int(ch)
                elif c==5 :
                    row[5]=ch
            rows.append(row)
            

    with open ("expenses.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(rows)

    if found==False:
        print("No matching expense found to change.")
    else:
        print("Expense updated successfully.")


def delete_expense():
    with open ("expenses.csv","r") as f:
        reader=csv.reader(f)
        rows=[]
        s=input("Enter expense id:")
        header=next(reader)
        rows.append(header)
        found=False
        for row in reader:
            if row[0]==s:
                found=True
            else:
                rows.append(row)
                continue
        
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if found==False:
        print("No matching expense to delete.")
    else:
        print("Expense deleted successfully.")
        
