from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class FileEncryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_file(self, file_path):
        cipher = AES.new(self.key, AES.MODE_EAX)
        with open(file_path, 'rb') as f:
            plaintext = f.read()

        ciphertext, tag = cipher.encrypt_and_digest(plaintext)

        file_out = file_path + ".enc"
        with open(file_out, 'wb') as f:
            for x in (cipher.nonce, tag, ciphertext):
                f.write(x)
        print(f"File encrypted: {file_out}")
        return file_out

    def decrypt_file(self, encrypted_file_path, output_path):
        with open(encrypted_file_path, 'rb') as f:
            nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)

        with open(output_path, 'wb') as f:
            f.write(plaintext)
        print(f"File decrypted: {output_path}")
