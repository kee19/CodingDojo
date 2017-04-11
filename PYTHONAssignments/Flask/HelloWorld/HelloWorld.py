from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('HelloWorld.html')

    
@app.route('/good_day')
def good_day():
    return render_template('good_day.html')

app.run(debug=True)
