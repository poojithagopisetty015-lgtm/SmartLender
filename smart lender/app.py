from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    income = int(request.form["income"])
    loan = int(request.form["loan"])
    credit = request.form["credit"]
    employment = request.form["employment"]

    if income >= 50000 and credit == "Good":
        status = "✅ Loan Approved"
        reason = "Applicant has good income and credit history."
        color = "green"

    elif income >= 30000 and employment == "Salaried":
        status = "🟡 Loan Under Review"
        reason = "Application needs further verification."
        color = "orange"

    else:
        status = "❌ Loan Rejected"
        reason = "Income or credit history is not sufficient."
        color = "red"

    return render_template(
        "index.html",
        status=status,
        reason=reason,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)