import os

def read_file():
    # Specified folder for files
    safe_folder = "./uploads"
    
    # Accepts filename directly from user without validation
    filename = input("Enter the filename to read: ")
    
    # Insecure path construction vulnerable to traversal (e.g., ../../etc/passwd)
    file_path = os.path.join(safe_folder, filename)
    
    try:
        with open(file_path, 'r') as file:
            print("\n--- File Contents ---")
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    read_file()
