"""
Simple "Hello, World" application using Flask
"""

from flask import Flask

from Calculator import quadratic


app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "some secret string here"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()