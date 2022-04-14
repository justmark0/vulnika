from flask import *
import os

app = Flask(__name__)

app.config["CLIENT_IMAGES"] = '/app/files'

@app.route("/", methods=["GET"])
def index():
    return render_template('main.html')


@app.route("/static/<name>", methods=["GET"])
def static_files(name):
    os.system(f'echo \'user requested {name}\' >> log.txt')
    with open(f'/app/files/{name}') as f:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=name, as_attachment=True, path=f'/app/files/{name}')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9998)
