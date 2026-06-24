import os

import shutil



def organize_folder(target_folder):

    print(f"--- 📂 Organizing Folder: {target_folder} ---")

    

    # Define which extensions go into which folders

    file_types = {

        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],

        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],

        "Audio": [".mp3", ".wav", ".flac"],

        "Videos": [".mp4", ".mkv", ".mov"],

        "Archives": [".zip", ".tar", ".rar", ".7z"]

    }

    

    # Check if the folder actually exists

    if not os.path.exists(target_folder):

        print("❌ Error: That folder path does not exist!")

        return



    # Loop through every file inside the target folder

    for filename in os.listdir(target_folder):

        file_path = os.path.join(target_folder, filename)

        

        # Skip if it's a folder, we only want to move files

        if os.path.isdir(file_path):

            continue

            

        # Extract the file extension (e.g., '.pdf') and make it lowercase

        _, extension = os.path.splitext(filename)

        extension = extension.lower()

        

        moved = False

        # Figure out which folder the file belongs to

        for folder_name, extensions in file_types.items():

            if extension in extensions:

                # Create the destination folder if it doesn't exist yet

                destination_folder = os.path.join(target_folder, folder_name)

                os.makedirs(destination_folder, exist_ok=True)

                

                # Move the file

                shutil.move(file_path, os.path.join(destination_folder, filename))

                print(f"📁 Moved: {filename} ➡️ {folder_name}/")

                moved = True

                break

                

        # If the file extension didn't match any category, put it in 'Others'

        if not moved and extension != "":

            other_folder = os.path.join(target_folder, "Others")

            os.makedirs(other_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(other_folder, filename))

            print(f"📁 Moved: {filename} ➡️ Others/")



    print("\n🎉 Folder successfully organized!")



if __name__ == "__main__":

    # REPLACE THIS with the actual path to a folder you want to clean up

    # Example for Windows: "C:/Users/YourName/Downloads/TestFolder"

    # Example for Mac/Linux: "/Users/YourName/Downloads/TestFolder"

    folder_to_clean = "./TestFolder" 

    organizer_folder(folder_to_clean)



