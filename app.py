#! /usr/bin/python
# -*- coding:utf-8 -*-
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def accueil():
    lights = ["blue", "red"]
    return render_template('view.html', titre="Light Switcher", lights=lights)

@app.route('/switch', methods=['POST'])
def switch():
    os.system("gpio write 0 " + ("1" if os.popen("gpio read 0").readline()[:-1] == "0" else "0"));
    return ""

if __name__ == '__main__':
    app.run(debug=True)
    app.secret_key = "ksodjvs46g4gk9$f:88"
