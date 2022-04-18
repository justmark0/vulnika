from flask import *
import os

app = Flask(__name__)

app.config["CLIENT_IMAGES"] = '/app/files'

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    
    if request.method == 'GET':
        with open("feedback.txt", "r") as file:
            message = file.read()

    if request.method == 'POST':
        message = request.form['feedback']
        with open("feedback.txt", "w") as file:
            file.write(message)

    return render_template('main.html', feed_mess=escape(message))


@app.route("/static", methods=["GET"])
def static_files():
    src = request.args.get("src")
    return send_from_directory(app.config["CLIENT_IMAGES"], src)


@app.route("/feedback", methods=["POST"])
def feedback():
    if request.method == 'POST':
        data = request.get_json().get('feedback')
        with open("feedback.txt", "w") as file:
            file.write(data)
    return 'ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9998)
