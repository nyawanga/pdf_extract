from flask import Flask, request, flash, send_from_directory
from flask import redirect, url_for, render_template, jsonify, send_file
from werkzeug import secure_filename
import patents
import os
import json

UPLOAD_FOLDER ='./uploads'
DOWNLOAD_FOLDER = './download'
TEMP_FOLDER = './temp'
ALLOWED_EXTENSIONS = {'txt','csv'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['TEMP_FOLDER'] = TEMP_FOLDER

def allowed_files(filename):
    return "." in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route('/uploader',methods=["POST","GET"])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('no file attached')
            return redirest(request.url)

        file = request.files['file']
        if(file.filename == ''):
            flash('no file uploaded')
            return redirect(request.url)
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['TEMP_FOLDER'], filename))
            with app.open_resource(os.path.join(app.config['TEMP_FOLDER'], filename), "r") as f:
                text = f.read()
            return_data = patents.process_data(text)
            with open('./download/processed_data.json', 'w') as outfile:
                json.dump(return_data, outfile)
            # return (json.dumps(return_data, "w"))
            # json_file = json.dumps(return_data)
            # , mimetype='application/json',
            #     filename="downloads.json")
            #     )

            # result_file = secure_filename()
            # json_file.save(os.path.join(app.config['UPLOAD_FOLDER'], json_file))
            # return jsonify(str(return_data))
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], result_file))

        return redirect(url_for('download_file',filename='processed_data.json'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'],
                               filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4646, debug=False)

