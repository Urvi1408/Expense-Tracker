from flask import Flask, render_template, request, redirect, url_for,jsonify
import utils.expenses_manager as em 
import utils.visualization as visualization 
import utils.analysis as analysis
from datetime import datetime

app=Flask(__name__)

@app.route("/")
def home():
    success = request.args.get("success")

    total=analysis.total_expenses()
    average=analysis.average_expense()
    highest=analysis.highest_expense()
    line=visualization.daily_expense_lg()
    cat=visualization.category_pie()
    month=visualization.monthly_bar()
    exp=visualization.top_expenses()
    mode=visualization.payment_mode_bar()
    transaction=analysis.total_transaction()

    return render_template("index.html",total=total,average=average,highest=highest,transaction=transaction,line=line ,cat=cat, month=month ,exp=exp,mode=mode,success=success)


@app.route("/add_expense",methods=["GET","POST"])
def add_expense():
    if request.method=="POST":
        date=request.form["date"]
        from datetime import datetime
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")
        category=request.form["category"]
        description=request.form["description"]
        amount=float(request.form["amount"])
        mode=request.form["mode"]
        
        em.addexpenses(date,category,description,amount,mode)
        return redirect(url_for("home",success="1"))

    return render_template("add_expense.html")

@app.route("/history",methods=["GET","POST"])
def history():
    choice=request.args.get("choice",type=int)
    search=request.args.get("search","")
    if search:
        view= em.search_expenses(choice, search)
    else:
        view=em.view_expenses()

    return render_template("history.html",view=view,search=search)


@app.route("/analytics")
def analytics():
    lowest=analysis.lowest_expense()
    daily=analysis.avg_daily()
    month=analysis.avg_monthly()
    top=analysis.top_spending()
    tot=analysis.daily_expenses().tail(5)
    cat=analysis.category_wise_expense()
    payment=analysis.payment_mode_analysis()
    return render_template("analytics.html", lowest=lowest,daily=daily,month=month,top=top,tot=tot,cat=cat,payment=payment)

if __name__ =="__main__":
    app.run(debug=True)