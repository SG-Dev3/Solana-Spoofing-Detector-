from flask import Flask, render_template, request
from data_fetcher import fetch_transactions
from analyzer import detect_spoofing
from database import save_result
from alerts import generate_alert

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        contract_address = request.form["contract_address"]
        data = fetch_transactions(contract_address)
        result = detect_spoofing(data)
        save_result(contract_address, result)
        generate_alert(contract_address, result)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
