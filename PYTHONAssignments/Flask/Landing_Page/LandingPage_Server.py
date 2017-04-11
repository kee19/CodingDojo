from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template ('landing_page.html',greeting='Welcome to the Landing Page!')


@app.route('/ninjas')
def ninjas():
    return render_template
    ('ninjas.html')

@app.route('dojos/new')
def dojos():
    return render_template
    ('dojos.html')

app.run(debug=True)