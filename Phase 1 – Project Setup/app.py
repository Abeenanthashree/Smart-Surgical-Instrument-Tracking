from flask import Flask, render_template

app = Flask(__name__)

# ---------------- Home ---------------- #

@app.route("/")
def home():
    return render_template("index.html")

# ---------------- Login ---------------- #

@app.route("/login")
def login():
    return render_template("login.html")

# ---------------- Dashboard ---------------- #

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ---------------- Inventory ---------------- #

@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

# ---------------- Sterilization ---------------- #

@app.route("/sterilization")
def sterilization():
    return render_template("sterilization.html")

# ---------------- Operating Theatre ---------------- #

@app.route("/operating_theatre")
def operating_theatre():
    return render_template("operating_theatre.html")

# ---------------- Reports ---------------- #

@app.route("/reports")
def reports():
    return render_template("reports.html")

# ---------------- History ---------------- #

@app.route("/history")
def history():
    return render_template("history.html")


if __name__ == "__main__":
    app.run(debug=True)
