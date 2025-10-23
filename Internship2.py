#Move all .jpg file to a new folder

import os
import shutil

#Source and destination folders
source_folder=r"C:\Users\Sanjana\Pictures"
destination_folder=r"C:\Users\Sanjana\Pictures\about-banner.png"

#create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedir(destination_folder)

#Move all jpg files
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        src_path=os.path.join(source_folder,file_name)
        dst_path=os.path.join(destination_folder,file_name)
        shutil.move(src_path,dst_path)
        print(f"Moved:{file_name}")
print("All .jpg files moved successfully!")
