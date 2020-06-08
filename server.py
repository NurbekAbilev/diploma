from flask import Flask
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/path/to/tesseracdt/executable'

from os import listdir
from os.path import isfile, join

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, W'  

if __name__ == "__main__":
    app.run(host='0.0.0.0')


    

# @app.route('/extract_data')
# def hello_world():
#     # Get image from the request
#     imagefile = flask.request.files.get('imagefile', '')
#     # Convert image to text
#     text = pytesseract.image_to_string(imagefile,lang='rus+kaz+eng')
#     # Extract valueable data from tensorflow Neral Network
#     value = model.predict(text)
    
#     return jsonify({
#         "status": "ok",
#         "value" : value
#     })    
    