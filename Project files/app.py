from flask import Flask, render_template, request 


app = Flask(__name__) # initializng the flask app


@app.route('/')
def index():
    return render_template('index.html')

    if __name__ == '_main_':
        app.run(debug = True, port = 8000)