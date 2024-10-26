from flask import Flask, request, render_template
import os
from ipfs import IPFSClient
from blockchain import Blockchain

app = Flask(__name__)
ipfs_client = IPFSClient()
blockchain = Blockchain()
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    # Upload to IPFS
    ipfs_hash = ipfs_client.upload_file(file_path)
    
    # Store in blockchain
    blockchain.create_block(len(blockchain.chain), {'file_name': file.filename, 'ipfs_hash': ipfs_hash})
    
    return 'File uploaded and stored in IPFS! Hash: ' + ipfs_hash

@app.route('/download', methods=['POST'])
def download_file():
    ipfs_hash = request.form['ipfs_hash']
    
    # Download the file from IPFS
    file_obj = ipfs_client.download_file(ipfs_hash)
    
    # File is saved to local storage
    return f'File {file_obj.name} downloaded from IPFS!'

if __name__ == '__main__':
    app.run(debug=True)
