from flask import Flask, render_template
from flask_wtf import FlaskForm
from doc_copy import classify
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
app.config["UPLOAD_FOLDER"] = r"E:\Document_Classification"


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/', methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(
            os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], secure_filename("testdocument.pdf")))
        return "File has been Uploaded" and classify()
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
