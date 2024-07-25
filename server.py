# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:15:18 2024

@author: ds448
"""

from server_app import app_func
from threading import Thread
from flask import Flask

thread = Thread(target = app_func)

app = Flask(__name__)

@app.route("/")
def run_server():
    if not thread.is_alive():
        thread.start()
    else:
        pass
    return 'Server is running...'

if __name__== '__main__':
    app.run(debug=True)