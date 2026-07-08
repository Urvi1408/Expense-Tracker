import matplotlib.pyplot as plt
import io
import base64
import utils.analysis as an

def category_pie():
    data=an.category_wise_expense()
    plt.figure(figsize=(10,10))
    colors =["#2563EB", 
        "#60A5FA",   
        "#93C5FD",   
        "#BFDBFE",   
        "#1D4ED8",   
        "#3B82F6"   
        ]
    wedges, texts, autotexts = plt.pie(
        data.values,
        labels=data.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors
    )

    for text in texts:
        text.set_fontsize(14)

    for autotext in autotexts:
        autotext.set_fontsize(13)
    plt.pie(data.values, labels=data.index,autopct="%1.1f%%")
    plt.tight_layout()

    buffer=io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    graph=base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return graph 


def category_bar():
    data=an.category_wise_expense()
    plt.figure(figsize=(12,6))
    plt.bar(data.index,data.values)
    plt.xlabel("Category",fontsize=15)
    plt.ylabel("Amount",fontsize=15)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.tight_layout()

    buffer=io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    graph=base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return graph 

def payment_mode_bar():
    data=an.payment_mode_analysis()
    plt.figure(figsize=(12,6))
    plt.bar(data.index,data.values)
    plt.xlabel("Payment Mode",fontsize=15)
    plt.ylabel("Amount",fontsize=15)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.tight_layout()

    buffer=io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    graph=base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return graph 

def daily_expense_lg():
    data=an.daily_expenses()
    plt.figure(figsize=(12,6))
    plt.plot(data.index,data.values,marker="o",markerfacecolor="blue",color="black")
    plt.xlabel("Date",fontsize=15)
    plt.ylabel("Amount",fontsize=15)
    plt.xticks(rotation=45,fontsize=13)
    plt.yticks(fontsize=13)
    plt.tight_layout()

    buffer=io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    graph=base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return graph

def monthly_bar():
    data=an.monthly_expenses()
    plt.figure(figsize=(12,6))
    plt.bar(data.index,data.values)
    plt.xlabel("Month",fontsize=15)
    plt.ylabel("Amount",fontsize=15)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.tight_layout()

    buffer=io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    graph=base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return graph 

def top_expenses():
    data=an.highest5_expenses()
    plt.figure(figsize=(12,6))
    plt.bar(data["description"],data["amount"])
    plt.xticks(rotation=30)
    plt.xlabel("Category",fontsize=15)
    plt.ylabel("Amount",fontsize=15)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.tight_layout()

    buffer=io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    graph=base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return graph 