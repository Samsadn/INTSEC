import hashlib
import os

def compute_checksum(filename):
    """Computes the SHA-256 checksum of a file."""
    hasher = hashlib.sha256()
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def compare_directories(dir1, dir2):
    """Compares files in two directories based on their names and checksums."""
    for filename in os.listdir(dir1):
        filepath1 = os.path.join(dir1, filename)
        filepath2 = os.path.join(dir2, filename)

        if os.path.isfile(filepath1) and os.path.isfile(filepath2):
            checksum1 = compute_checksum(filepath1)
            checksum2 = compute_checksum(filepath2)

            if checksum1 == checksum2:
                print(f"{filename}: Checksums match.")
            else:
                print(f"{filename}: Checksums do not match!")
        else:
            print(f"{filename}: File not found in both directories.")

if __name__ == "__main__":
    dir1 = input("Enter the first directory: ")
    dir2 = input("Enter the second directory: ")
    compare_directories(dir1, dir2)