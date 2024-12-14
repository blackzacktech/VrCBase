import os
import json

def list_folders_and_images(root_dir=".", ignore_list=None):
    if ignore_list is None:
        ignore_list = []

    folders = []
    images = []
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}

    for root, dirs, files in os.walk(root_dir):
        # Filter out directories to ignore
        dirs[:] = [d for d in dirs if not any(os.path.relpath(os.path.join(root, d), root_dir).startswith(ignore) for ignore in ignore_list)]
        
        for dir_name in dirs:
            folder_path = os.path.relpath(os.path.join(root, dir_name), root_dir)
            if not any(folder_path.startswith(ignore) for ignore in ignore_list):
                folders.append(folder_path)
        for file_name in files:
            if any(file_name.lower().endswith(ext) for ext in image_extensions):
                file_path = os.path.relpath(os.path.join(root, file_name), root_dir)
                if not any(file_path.startswith(ignore) for ignore in ignore_list):
                    images.append(file_path)
    
    return {"folders": folders, "images": images}

root_directory = "."  # Specify root directory here
ignore_list = [".git", ".github", "index.html"]  # Add paths to ignore here
data = list_folders_and_images(root_directory, ignore_list)

# Save to a JSON file
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been written to data.json")