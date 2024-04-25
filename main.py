import os
import shutil

# If you right click on anything in the downloads folder, you'll see that the path is C:\Users\username\Downloads
# We need to save the location of the downloads folder in a variable
# https://docs.python.org/3/library/os.path.html#os.path.expanduser
USER_DIRECTORY = os.path.expanduser("~")  # This will get the path of the user's directory
DOWNLOADS_PATH = os.path.join(USER_DIRECTORY, "Downloads")

DOWNLOAD_FOLDERS = {
    "Images": ["png", "jpg", "svg", "webp"],
    "PowerPoints": ["pptx", "ppt"],
    "Excel": ["xlsx", "xls", "csv"],
    "Documents": ["docx", "doc", "pdf"],
    "Zip": ["zip", "rar", "7z"],
    "Videos": ["mp4"],
    "Music": ["mp3"],
}
UNCATOGORIZED_FOLDER = "Uncatogorized"
OTHER_DOWNLOADS_FOLDER = "Others"


def where_am_i():
    # https://docs.python.org/3/library/os.html#os.getcwd
    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")


def change_to_downloads_folder():
    where_am_i()

    # https://docs.python.org/3/library/os.html#os.chdir
    print("Changing to downloads folder...")
    os.chdir(DOWNLOADS_PATH)
    where_am_i()
    input(f"Changed to downloads folder: {DOWNLOADS_PATH}. Press enter to continue sorting here...")


def get_files_in_folder():
    # https://docs.python.org/3/library/os.html#os.listdir
    all_files = os.listdir()
    n_files = len(all_files)
    print(f"Number of files in downloads: {n_files}")
    return all_files, n_files


def create_folder_if_not_exists(folder_name):
    # https://docs.python.org/3/library/os.path.html#os.path.exists
    if not os.path.exists(folder_name):
        # https://docs.python.org/3/library/os.html#os.mkdir
        os.mkdir(folder_name)
        print(f"Created folder: {folder_name}")


def organize(file):
    # Is it a file or a folder?
    if os.path.isfile(file):
        # https://docs.python.org/3/library/os.path.html#os.path.splitext
        filename, extension = os.path.splitext(file)
        # Remove the dot from the extension
        # https://docs.python.org/3/library/stdtypes.html#str.replace
        # https://docs.python.org/3/library/stdtypes.html#str.lower
        extension = extension.replace(".", "").lower()
        current_file_path = os.path.join(DOWNLOADS_PATH, file)

        # Check if the extension is in the DOWNLOAD_FOLDERS dictionary
        is_sorted = False
        for sort_folder, sort_extension in DOWNLOAD_FOLDERS.items():
            if extension in sort_extension:
                create_folder_if_not_exists(sort_folder)
                # https://docs.python.org/3/library/shutil.html#shutil.move
                new_file_path = os.path.join(DOWNLOADS_PATH, sort_folder, file)
                shutil.move(current_file_path, new_file_path)
                print(f"Moved '{file}' to '{sort_folder}' folder.")
                is_sorted = True
                break

        if not is_sorted:
            create_folder_if_not_exists(UNCATOGORIZED_FOLDER)
            new_file_path = os.path.join(DOWNLOADS_PATH, UNCATOGORIZED_FOLDER, file)
            shutil.move(current_file_path, new_file_path)
            print(f"Moved '{file}' to '{UNCATOGORIZED_FOLDER}' folder.")
    else:
        print(f"{file} is a folder. Moving to '{OTHER_DOWNLOADS_FOLDER}' folder.")
        new_file_path = os.path.join(DOWNLOADS_PATH, OTHER_DOWNLOADS_FOLDER, file)
        shutil.move(file, new_file_path)


if __name__ == "__main__":
    input("Welcome to the downloads organizer! Press enter to continue...")
    change_to_downloads_folder()
    all_files, n_files = get_files_in_folder()

    # https://docs.python.org/3/library/functions.html#enumerate
    for i, file in enumerate(all_files):
        # https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
        print(f"[{i + 1}/{n_files}] Organizing {file}")

        # https://docs.python.org/3/tutorial/errors.html#handling-exceptions
        try:
            organize(file)
        except Exception as e:
            print(f"Error organizing {file}: {e}")

    input("Done! Press enter to exit...")
