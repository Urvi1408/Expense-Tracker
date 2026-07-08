import utils.expenses_manager as em
import utils.visualization as visualization 
import utils.analysis as analysis

print("Welcome to the Expense Manager!")

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Analysis")
    print("7. Visualization")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        em.addexpenses()

    elif choice == 2:
        em.view_expenses()

    elif choice == 3:
        em.search_expenses()

    elif choice == 4:
        em.change_expenses()

    elif choice == 5:
        em.delete_expense()

    elif choice==6:
         while True:

             print("""
                ========== Analysis ==========
                1. Total Expenses
                2. Category-wise Expenses
                3. Highest Expense
                4. Lowest Expense
                5. Average Expense
                6. Payment Mode Analysis
                7. Total Transactions
                8. Monthly Expenses
                9. Daily Expenses
                10. Top Spending Category
                11. Top 5 Highest Expenses
                12. Average Daily Expense
                13. Sort by Amount (Ascending)
                14. Sort by Amount (Descending)
                15. Sort by Date
                16. Category Percentage
                17. Back
                ==============================
                """)

             ch = int(input("Enter your choice: "))

             if ch == 1:
                print("Total Expenses: ₹", analysis.total_expenses())

             elif ch == 2:
                print(analysis.category_wise_expense())

             elif ch == 3:
                print(analysis.highest_expense())

             elif ch == 4:
                print(analysis.lowest_expense())

             elif ch == 5:
                print("Average Expense: ₹", analysis.average_expense())

             elif ch == 6:
                print(analysis.payment_mode_analysis())

             elif ch == 7:
                print("Total Transactions:", analysis.total_transaction())

             elif ch == 8:
                print(analysis.monthly_expenses())

             elif ch == 9:
                print(analysis.daily_expenses())

             elif ch == 10:
                analysis.top_spending()

             elif ch == 11:
                print(analysis.highest5_expenses())

             elif ch == 12:
                print("Average Daily Expense: ₹", analysis.avg_daily())

             elif ch == 13:
                print(analysis.sort_asc())

             elif ch == 14:
                print(analysis.sort_desc())

             elif ch == 15: 
                print(analysis.sort_by_date())

             elif ch == 16:
                print(analysis.category_percentage())

             elif ch == 17:
                break

             else:
                print("Invalid Choice.")

    elif choice==7:
        while True:

            print("""
                ========== Visualization ==========

                1. Category Pie Chart
                2. Category Bar Graph
                3. Payment Mode Bar Graph
                4. Daily Expense Line Graph
                5. Monthly Expense Bar Graph
                6. Top 5 Highest Expenses
                7. Back

                ===================================
                """)
            ch = int(input("Enter your choice: "))

            if ch == 1:
                visualization.category_pie()

            elif ch == 2:
                visualization.category_bar()

            elif ch == 3:
                visualization.payment_mode_bar()

            elif ch == 4:
                visualization.daily_expense_lg()

            elif ch == 5:
                visualization.monthly_bar()

            elif ch == 6:
                visualization.top_expenses()

            elif ch == 7:
                break

            else:
                print("Invalid Choice.")
       

    elif choice == 8:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice.")