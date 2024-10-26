import ipfshttpclient

class IPFSClient:
    def __init__(self):
        self.client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
 # Connect to local IPFS daemon

    def upload_file(self, file_path):
        res = self.client.add(file_path)
        return res['Hash']  # Return the IPFS hash

    def download_file(self, ipfs_hash):
        return self.client.get(ipfs_hash)  # Download the file by its hash
