import os
import hashlib
import json

class FileIntegrityChecker:
    def __init__(self, file_path, hash_file="file_hash.json"):
        """
        Initializes the FileIntegrityChecker for a single file.

        :param file_path: The full path of the file to monitor.
        :param hash_file: The file to store the hash value.
        """
        self.file_path = file_path
        self.hash_file = hash_file
        self.file_hash = None  # Stores the last known hash
        self.load_hash()

    def calculate_hash(self):
        """
        Calculates the SHA-256 hash of the file.

        :return: The hash value as a hexadecimal string, or None if the file doesn't exist.
        """
        sha256 = hashlib.sha256()
        if not os.path.exists(self.file_path):
            print(f"Error: File '{self.file_path}' not found!")
            return None

        try:
            with open(self.file_path, "rb") as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except (OSError, IOError) as e:
            print(f"Error reading {self.file_path}: {e}")
            return None

    def load_hash(self):
        """
        Loads the previously stored hash value from a JSON file.
        """
        if os.path.exists(self.hash_file):
            try:
                with open(self.hash_file, "r") as f:
                    stored_data = json.load(f)
                    self.file_hash = stored_data.get(self.file_path)
            except (OSError, IOError, json.JSONDecodeError) as e:
                print(f"Error loading hash file: {e}")

    def save_hash(self, new_hash):
        """
        Saves the current hash value to a JSON file.
        """
        try:
            with open(self.hash_file, "w") as f:
                json.dump({self.file_path: new_hash}, f, indent=4)
        except (OSError, IOError) as e:
            print(f"Error saving hash file: {e}")

    def monitor_changes(self):
        """
        Checks if the file has been modified or deleted.

        :return: A dictionary with the status of the file.
        """
        current_hash = self.calculate_hash()

        if current_hash is None:
            status = "File Deleted"
        elif self.file_hash is None:
            status = "First Scan - File Added"
        elif self.file_hash != current_hash:
            status = "File Modified"
        else:
            status = "No Changes"

        # Update stored hash if file exists
        if current_hash:
            self.file_hash = current_hash
            self.save_hash(current_hash)

        return status

if __name__ == "__main__":
    # 🔹 Specify the file to monitor
    file_to_monitor = r"file_path"
    print(f"Monitoring changes in: {file_to_monitor}\n")

    checker = FileIntegrityChecker(file_to_monitor)
    change_status = checker.monitor_changes()

    print(f"Status: {change_status}")
