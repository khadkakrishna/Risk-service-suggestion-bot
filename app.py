from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def home(): 
    return render_template('index.html')

@app.route("/policies")
def policies(): 
    return render_template('policies.html')

@app.route("/rules")
def rules(): 
    return render_template('rules.html')


if __name__ == "__main__":
    app.run(debug=True)