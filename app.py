from flask import Flask,render_template,jsonify
import utils.expenses_manager as em
import utils.visualization as visualization 
import utils.analysis as analysis

app=Flask(__name__)

@app.route("/")
def home():
    total=analysis.total_expenses()
    average=analysis.average_expense()
    highest=analysis.highest_expense()
    line=visualization.daily_expense_lg()
    cat=visualization.category_pie()
    month=visualization.monthly_bar()
    exp=visualization.top_expenses()
    mode=visualization.payment_mode_bar()

    return render_template("index.html",total=total,average=average,highest=highest,line=line ,cat=cat, month=month ,exp=exp,mode=mode)

if __name__ =="__main__":
    app.run(debug=True)