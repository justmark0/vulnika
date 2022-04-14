from flask import *
import os

app = Flask(__name__)

app.config["CLIENT_IMAGES"] = '/app/files'

@app.route("/", methods=["GET"])
def index():
    return render_template('main.html')


@app.route("/static", methods=["GET"])
def static_files():
    src = request.args.get("src")
    return send_file(f'/app/files/{src}', as_attachment=True)


@app.route("/feedback", methods=["POST"])
def feedback():
    if request.method == 'POST':
        data = request.get_json()
        feedback = data.get('feedback')
        os.system(f'echo \'user feedback: {feedback}\' >> feedback.txt')
    return 'ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9998)
