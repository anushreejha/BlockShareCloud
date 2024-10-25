import ipfshttpclient

class IPFSClient:
    def __init__(self):
        self.client = ipfshttpclient.connect()

    def upload_file(self, file_path):
        result = self.client.add(file_path)
        print(f"File uploaded: {result['Hash']}")
        return result['Hash']

    def download_file(self, file_hash, output_path):
        self.client.get(file_hash, target=output_path)
        print(f"File downloaded: {output_path}")
