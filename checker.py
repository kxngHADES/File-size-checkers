import os
import humanize

def get_files_with_size(path, min_size):
    large_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size > min_size:
                    large_files.append((file_path, file_size))
            except (FileNotFoundError, PermissionError):
                continue
    return large_files

def print_large_files(files):
    for file_path, file_size in sorted(files, key=lambda x: x[1], reverse=True):
        print(f"{file_path}: {humanize.naturalsize(file_size)}")

if __name__ == "__main__":
    
    min_size = 2048  * 1024 * 1024   #fist number is size in mbs
    path = "C:\\" #change letter for driver

    print("Scanning for large files...")
    large_files = get_files_with_size(path, min_size)
    print(f"Found {len(large_files)} files larger than {humanize.naturalsize(min_size)}:")
    print_large_files(large_files)
