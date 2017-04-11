from flask import Flask, render_template

app = Flask(__name__)

@app.router('/')



def good_day():
    return render_template('good_day.html')

    app.run(debug=True)

    @app.route('/good_nite')
    def good():
        return render_template('good_nite.html')