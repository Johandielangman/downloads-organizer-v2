import os
import shutil
import time
from progress.bar import Bar
from constants import (
    UNCATOGORIZED_FOLDER,
    OTHER_DOWNLOADS_FOLDER,
)


class DownloadsOrganizer:
    def __init__(self, downloads_path: str, config: dict) -> None:
        self.downloads_path = downloads_path
        self.downloads_config = config
        self.num_files = 0

    def change_to_downloads_folder(self) -> None:
        os.chdir(self.downloads_path)
        n_files = len(os.listdir())
        input(f"Your downloads folder is: '{self.downloads_path}'. There are {n_files} file(s)/folder(s) to look at! Press enter to continue sorting here...\n")

    def get_files_in_folder(self) -> tuple[list, int]:
        all_files = os.listdir()
        n_files = len(all_files)
        print(f"Number of files in downloads: {n_files}")
        return all_files, n_files

    def create_folder_if_not_exists(self, folder_name: str) -> None:
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

    def move_without_overwrite(self, current_file_path: str, new_file_path: str) -> None:
        _, current_file = os.path.split(current_file_path)
        new_dir, _ = os.path.split(new_file_path)

        files_in_new_dir = os.listdir(new_dir)

        counter = 1
        if current_file in files_in_new_dir:
            new_filename_original, new_filext = os.path.splitext(current_file)

            new_filename = f"{new_filename_original} ({counter}){new_filext}"
            while os.path.exists(os.path.join(new_dir, new_filename)):
                counter += 1
                new_filename = f"{new_filename_original} ({counter}){new_filext}"
            shutil.move(current_file_path, os.path.join(new_dir, new_filename))
        else:
            shutil.move(current_file_path, new_file_path)

    def organize_file(self, file: str) -> None:
        if os.path.isfile(file):
            filename, extension = os.path.splitext(file)
            extension = extension.replace(".", "").lower()
            current_file_path = os.path.join(self.downloads_path, file)

            # Check if the extension is in the DOWNLOAD_FOLDERS dictionary
            is_sorted = False
            for sort_folder, sort_extension in self.downloads_config.items():
                if extension in sort_extension:
                    self.create_folder_if_not_exists(sort_folder)
                    # https://docs.python.org/3/library/shutil.html#shutil.move
                    new_file_path = os.path.join(self.downloads_path, sort_folder, file)
                    self.move_without_overwrite(current_file_path, new_file_path)
                    is_sorted = True
                    break

            if not is_sorted:
                self.create_folder_if_not_exists(UNCATOGORIZED_FOLDER)
                new_file_path = os.path.join(self.downloads_path, UNCATOGORIZED_FOLDER, file)
                self.move_without_overwrite(current_file_path, new_file_path)
        else:
            new_file_path = os.path.join(self.downloads_path, OTHER_DOWNLOADS_FOLDER, file)

            # Don't move folders that are keys of the self.downloads_config dictionary or OTHER_DOWNLOADS_FOLDER
            if (
                file not in self.downloads_config.keys() and
                file != OTHER_DOWNLOADS_FOLDER
            ):
                other_files = os.listdir(os.path.join(self.downloads_path, OTHER_DOWNLOADS_FOLDER))
                if file not in other_files:
                    shutil.move(file, new_file_path)

    def organize_files(self) -> None:
        self.change_to_downloads_folder()
        all_files, num_files = self.get_files_in_folder()
        with Bar('Processing', max=num_files) as bar:
            for file in all_files:
                self.organize_file(file)
                time.sleep(0.1)
                bar.next()
