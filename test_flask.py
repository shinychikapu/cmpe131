from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello, CMPE131!"


@app.route("/<string:input>")
def view():
    return input

@ app.route("/<string:input>")
def hello(input):
    now = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    return '''
    <html>
        <head>
            <title>Home Page - my blog</title>
        </head>
        <body>
            <h1>Hello, ''' + input + '''!</h1>
            <b>Today is '''+ now + '''</b>
        </body>
        </html>'''
app.run()