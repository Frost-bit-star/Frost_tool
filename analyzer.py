import hashlib

def calculate_hash(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        md5_hash = hashlib.md5(file_data).hexdigest()
        sha256_hash = hashlib.sha256(file_data).hexdigest()
    return md5_hash, sha256_hash

file_path = "malware_sample.exe"
md5_hash, sha256_hash = calculate_hash(file_path)
print(f"MD5: {md5_hash}, SHA-256: {sha256_hash}")
