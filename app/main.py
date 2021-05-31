from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Welcome to StandupMonkey</h1><br><p>A self hosted slack bot to conduct standups &amp; generate reports.</p>"

