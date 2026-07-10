import pandas as pd
import numpy as np
import csv


def load_csv():
    df=pd.read_csv("data/expenses.csv")
    df["mode_of_payment"] = (
    df["mode_of_payment"]
        .str.strip()      
        .str.lower() 
    )
    return df

def total_expenses():
    df=load_csv()
    total=df["amount"].sum()
    return total

def category_wise_expense():
    df=load_csv()
    tot=df.groupby("category")["amount"].sum()
    return tot

def highest_expense():
    df=load_csv()
    high=df.loc[df["amount"].idxmax()]
    return {
            "amount": high["amount"],
            "category": high["category"],
            "description": high["description"],
            "date": high["date"]
            }

def lowest_expense():
    df=load_csv()
    low=df.loc[df["amount"].idxmin()]
    return {
        "amount": low["amount"],
        "category": low["category"],
        "description": low["description"],
        "date": low["date"]
    }

def average_expense():
    df=load_csv()
    av=df["amount"].mean()
    return av

def payment_mode_analysis():
    df=load_csv()
    pma=df.groupby("mode_of_payment")["amount"].sum()
    return pma

def sort_asc():
    df=load_csv()
    asc=df.sort_values("amount")
    return asc

def sort_desc():
    df=load_csv()
    des=df.sort_values("amount",ascending=False)
    return des

def sort_by_date():
    df=load_csv()
    df["date"]=pd.to_datetime(df["date"],dayfirst=True)
    sorted=df.sort_values(by="date")
    return sorted

# def search_category():
#     df=load_csv()
#     category=input("Enter category: ")
#     result = df[df["category"].str.strip().str.lower() == category.strip().lower()]
#     if result.empty:
#         print("No records found.")
#     else:
#         return result

# def search_mode():
#     df=load_csv()
#     mode=input("Enter the mode of payment: ")

#     result=df[df["mode_of_payment"].str.lower()==mode.lower()]

#     if result.empty:
#         print("No records found")
#     else:
#         return result

def total_transaction():
    df=load_csv()
    count=len(df)
    return count

def highest5_expenses():
    df=load_csv()

    top=df.nlargest(5,"amount")
    return top

def monthly_expenses():
    df=load_csv()
    df["date"]=pd.to_datetime(df["date"],dayfirst=True)
    monthly=df.groupby(df["date"].dt.month_name())["amount"].sum()
    return monthly

def category_percentage():
    df=load_csv()
    percent=(df.groupby("category")["amount"].sum() /df["amount"].sum())*100
    return percent

def daily_expenses():
    df=load_csv()
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    daily=df.groupby("date")["amount"].sum()
    return daily

def top_spending():
    df=load_csv()
    top = df.groupby("category")["amount"].sum()

    return top.idxmax()

def avg_daily():
    df=load_csv()
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    dav=df.groupby("date")["amount"].sum()
    davg=dav.mean()
    return davg

def avg_monthly():
    d=monthly_expenses()
    return d.mean()
