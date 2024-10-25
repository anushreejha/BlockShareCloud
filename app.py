from Crypto.Cipher import AES
import os
from flask import Flask, request, render_template

app = Flask(__name__)

def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    with open(file_path + '.enc', 'wb') as file:
        file.write(cipher.nonce)
        file.write(tag)
        file.write(ciphertext)

@app.route('/')
def home():
    return render_template('index.html')  # Main page template

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    
    key = os.urandom(16)  # Generate a random key
    encrypt_file(file_path, key)
    return 'File uploaded and encrypted!'

if __name__ == '__main__':
    app.run(debug=True)
