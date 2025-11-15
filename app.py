from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template("index.html", name=name)

if _name_ == "_main_":
    app.run(debug=True)
