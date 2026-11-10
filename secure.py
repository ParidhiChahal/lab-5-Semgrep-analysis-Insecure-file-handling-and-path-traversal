import os

def read_file_secure():
    safe_folder = os.path.abspath("./uploads")
    
    filename = input("Enter the filename to read: ")
    
    # Construct the absolute path
    target_path = os.path.abspath(os.path.join(safe_folder, filename))
    
    # Validate that the target path starts with the safe directory path
    if not target_path.startswith(safe_folder + os.sep):
        print("Security Alert: Path traversal attempt detected!")
        return

    try:
        with open(target_path, 'r') as file:
            print("\n--- File Contents ---")
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    read_file_secure()
