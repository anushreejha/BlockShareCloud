import ipfshttpclient
import os

class IPFSClient:
    def __init__(self):
        # Connect to local IPFS daemon
        self.client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')

    def upload_file(self, file_path):
        res = self.client.add(file_path)
        return res['Hash']  # Return the IPFS hash

    def download_file(self, ipfs_hash, download_folder):
        # Create the download folder if it doesn't exist
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Download the file from IPFS and save it in the download_folder
        self.client.get(ipfs_hash, target=download_folder)
        
        # Return the path of the downloaded file
        return os.path.join(download_folder, ipfs_hash)
