from flask import Flask, request
from pony.flask import Pony
from pony.orm import Database, Required
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
Pony(app)

db = Database()
db.bind(provider = "postgres", user = "postgres", password = "postgres", host = "localhost", database = "db")

class Avatars(db.Entity):
    avatar = Required(str)

db.generate_mapping(create_tables=True)

UPLOAD_FOLDER = 'static/imgs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "tidak ada file input"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return "file tidak diisi"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return filename
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
