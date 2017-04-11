from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def WhatsMyName():
    return render_template ('WhatsMyName.html')

app.run(debug=True)