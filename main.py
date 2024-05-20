import os

from utils.config import Config
from utils.organizer import DownloadsOrganizer
from utils.style import Banner
from constants import DOWNLOADS_PATH


if __name__ == "__main__":
    banners = Banner()
    banners.home()
    specific_folder = input("Welcome to the downloads organizer! Press enter to continue...\n")

    if (
        specific_folder and
        os.path.exists(os.path.join(DOWNLOADS_PATH, specific_folder))
    ):
        downloads_path = os.path.join(DOWNLOADS_PATH, specific_folder)
    else:
        downloads_path = DOWNLOADS_PATH

    config = Config()
    organizer = DownloadsOrganizer(
        downloads_path=downloads_path,
        config=config.get_config()
    )
    organizer.organize_files()

    banners.random_animal()
    input("Press enter to exit...")
