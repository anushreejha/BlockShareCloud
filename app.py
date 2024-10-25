from flask import Flask, request, jsonify
from uuid import uuid4
from blockchain import Blockchain
from ipfs_client import IPFSClient
from encryption import FileEncryptor
from Crypto.Random import get_random_bytes

app = Flask(__name__)

blockchain = Blockchain()
ipfs_client = IPFSClient()
encryptor = FileEncryptor(get_random_bytes(16))

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)

    encrypted_file = encryptor.encrypt_file(file_path)
    file_hash = ipfs_client.upload_file(encrypted_file)

    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    owner = str(uuid4())
    blockchain.create_block(proof, previous_hash, file_hash, owner)

    return jsonify({'message': 'File uploaded successfully', 'file_hash': file_hash}), 201

@app.route('/download/<file_hash>', methods=['GET'])
def download_file(file_hash):
    output_path = f"./downloads/{file_hash}"
    ipfs_client.download_file(file_hash, output_path)

    decrypted_file_path = output_path.replace('.enc', '')
    encryptor.decrypt_file(output_path, decrypted_file_path)

    return jsonify({'message': f'File downloaded and decrypted: {decrypted_file_path}'}), 200

if __name__ == '__main__':
    app.run(debug=True)
