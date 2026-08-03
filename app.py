from flask import Flask, render_template, request
from scam_detector import analyze_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    reasons = []

    if request.method == "POST":
        user_input = request.form["text"]
        result, reasons = analyze_text(user_input)

    return render_template("index.html", result=result, reasons=reasons)

if __name__ == "__main__":
    app.run(debug=True)
