from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Everyone, This application just print "It is our first ARGOCD Project'
