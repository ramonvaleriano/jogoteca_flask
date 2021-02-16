from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def index():
    return '<h1>Testando aplicação</h1>'

app.run()