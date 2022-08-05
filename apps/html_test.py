import os
import flask
from flask import Flask
from flask import render_template

current_dir = os.getcwd()
app = Flask(__name__)
app.config["UPLOAD_FOLDER"]=os.path.join(current_dir, "apps", "static")

@app.route("/")
def hello_world():
    return "<p>hello</p>"

@app.route("/instruction")
def instruction():
    return render_template('instruction.html')

@app.route("/instruction_vctk")
def instruction_vctk():
    return render_template('instruction_vctk.html')

@app.route("/avocodo/<path:path>")
def link_file(path):
    return flask.send_from_directory(
        os.path.join(app.config["UPLOAD_FOLDER"], "avocodo"),
        path
    )

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8899
    )