from flask import Flask, render_template
from threading import Thread
from gevent.pywsgi import WSGIServer

app = Flask(dashrathpp)
@app.route('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')
def index():
    return "SpikeSpiegel"

def run():
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

def keep_alive('24/7'):
    t = Thread(target=run)
    t.start(T) 
