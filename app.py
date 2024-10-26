from flask import Flask, request, render_template, send_file
import os
from ipfs import IPFSClient
from blockchain import Blockchain

app = Flask(__name__)
ipfs_client = IPFSClient()
blockchain = Blockchain()
UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

# Ensure upload and download directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

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
    
    # Download the file from IPFS and save it locally in the 'downloads' folder
    file_obj = ipfs_client.download_file(ipfs_hash, DOWNLOAD_FOLDER)  # Pass DOWNLOAD_FOLDER as second argument
    file_path = os.path.join(DOWNLOAD_FOLDER, ipfs_hash)  # Path where the file was saved

    if not os.path.exists(file_path):
        return f'Error: File {ipfs_hash} not found in local storage!'

    # Serve the file for download
    return send_file(file_path, as_attachment=True, download_name=f"{ipfs_hash}.file")

if __name__ == '__main__':
    app.run(debug=True)
