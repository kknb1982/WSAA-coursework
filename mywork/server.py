from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/books')
def getall():
    return "Get all books!"

@app.route('/hello')
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
