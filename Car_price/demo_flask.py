from flask import Flask

app = Flask(__name__)


@app.route('/myName')
def myName():
    return 'Bipul Kumar Shahi'

@app.route('/hello')
def hello():
    return 'Hello World'


app.run(host='0.0.0.0',port='5000')
