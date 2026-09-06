from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/resume")
def resume():
    resume_folder = os.path.join(app.root_path, "resume")

    return send_from_directory(
        resume_folder,
        "linuxresume.docx",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)