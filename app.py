from flask import Flask, redirect, session, render_template, request, flash, url_for

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        binary = str(request.form.get("binary"))
        is_binary = True
        digit = 0
        for bit in binary:
            if int(bit) != 0 and int(bit) != 1:
                is_binary = False
                digit = bit
        if not is_binary:
            return render_template("error.html", digit=digit)
        else:
            decimal = 0
            for i in range(len(binary)):
                decimal += int(binary[i])*(2**(len(binary)-i-1))
            return render_template("home.html", decimal=str(decimal))
    else:
        return render_template("home.html", decimal="")