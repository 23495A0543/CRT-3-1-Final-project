from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods =["GET"])
def homepage():
    return render_template("index.html")


app.run(debug=True)