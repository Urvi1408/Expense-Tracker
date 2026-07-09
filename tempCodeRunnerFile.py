@app.route("/history",methods=["GET","POST"])
def history():
    view=em.view_expenses()
    return render_template("history.html",view=view)