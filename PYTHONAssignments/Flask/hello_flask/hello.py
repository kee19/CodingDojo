from flask import Flask, render_template

app = Flask(__name__)

@app.router('/')




def hello_world():
  return render_template('HelloWorld.html')

  app.run(debug=True)

  @app.route('/success')
  def success():
    return render_template('success.html')