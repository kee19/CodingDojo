from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.run(debug=True)

@app.route('/')
def FormTest():
    return render_template("FormTest.html")


@app.route('/users', methods=['POST'])
def create_user():
    
    name = request.form['name']
    email = request.form['email']

    return render_template('success.html')

app.run(debug=True)
