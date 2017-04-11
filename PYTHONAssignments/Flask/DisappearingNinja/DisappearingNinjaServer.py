from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def DisappearingDojo():
    return render_template ('DisappearingDojo')

@app.route('/ninja')
def Ninja():
    return render_template(ninja.html)
