from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def dashboard():

    return render_template("index.html")

@app.route('/services')
def services():
    
    return render_template("services.html")
app.run(debug=True)