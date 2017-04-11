from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def DojoSurvey():
    return render_template ('DojoSurvey.html')

@app.route('/process', methods=['POST'])
def submit_form():
    Name = request.form["YourName"]
    DojoLocation = request.form["DojoLocation"]
    favoritelanguage = request.form["favoritelanguage"]

    return redirect('/result')

    
@app.route('/result')
def result():
    return render_template('result.html', template_name='YourName', template_location='DojoLocation', template_language='favoritelanguage')


app.run(debug=True)