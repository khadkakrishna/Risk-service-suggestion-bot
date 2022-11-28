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

file1 = open('data.dat', 'r')
suggestions_demo = file1.readlines()
print(suggestions_demo)

@app.route("/suggestions")
def suggestions(): 
    return render_template('suggestions.html', suggestions=suggestions_demo, suggestions_count=len(suggestions_demo))

if __name__ == "__main__":
    app.run(debug=True)