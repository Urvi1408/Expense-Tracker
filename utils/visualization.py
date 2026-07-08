import matplotlib.pyplot as plt
import utils.analysis as an

def category_pie():
    data=an.category_wise_expense()
    plt.figure(figsize=(5,5))
    plt.pie(data.values, labels=data.index,autopct="%1.1f%%")
    plt.title("Category-Wise Expenses")

    plt.show()


def category_bar():
    data=an.category_wise_expense()
    plt.figure(figsize=(8,5))
    plt.bar(data.index,data.values)
    plt.title("Category Wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()

def payment_mode_bar():
    data=an.payment_mode_analysis()
    plt.figure(figsize=(8,5))
    plt.bar(data.index,data.values)
    plt.title("Payment Mode Analysis")
    plt.xlabel("Payment Mode")
    plt.ylabel("Amount")

    plt.show()

def daily_expense_lg():
    data=an.daily_expenses()
    plt.figure(figsize=(10,5))
    plt.plot(data.index,data.values,marker="o",markerfacecolor="blue",color="black")
    plt.title("Daily Expenses")
    plt.xlabel("Date")
    plt.ylabel("Amount")

    plt.show()

def monthly_bar():
    data=an.monthly_expenses()
    plt.figure(figsize=(8,5))
    plt.bar(data.index,data.values)
    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount")

    plt.show()

def top_expenses():
    data=an.highest5_expenses()
    plt.figure(figsize=(8,5))
    plt.bar(data["description"],data["amount"])
    plt.xticks(rotation=30)
    plt.title("Top 5 Highest Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()