# BlockShareCloud : Blockchain-Based Decentralized Cloud Storage System

This project implements a simple decentralized cloud storage system with AES encryption using Flask. Users can upload files, which are then encrypted and stored securely.


## Setup

### 1. Clone the repository:
```bash
git clone <repository-url>
cd project
```
### 2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # For macOS
# On Windows use `venv\Scripts\activate`
```
### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```
### 4. Create the uploads directory: 
```bash
mkdir uploads
```
### 5. Run the application:
```bash
python app.py
```
### 6. To access the application, open your browser and go to:
```bash
python app.py
```

## Features
- **File Upload:** Users can upload files through a simple web interface.
- **AES Encryption:** Files are encrypted using AES encryption for secure storage.
- **Flask Framework:** The application is built using the Flask web framework, providing a lightweight and easy-to-use structure.

## How It Works
**1.** When a user uploads a file, it is temporarily saved in the uploads directory.
**2.** The application generates a random encryption key and uses it to encrypt the uploaded file.
**3.** The encrypted file is saved with the .enc extension, retaining the original filename for ease of identification.
