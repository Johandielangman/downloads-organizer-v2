import argparse
import os

from utils.organizer import DownloadsOrganizer
from utils.config import Config
from utils.style import Banner
from constants import (
    DOWNLOADS_PATH
)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Organize your downloads folder!")
    parser.add_argument(
        "--run-non-interactive",
        "-r",
        action="store_true",
        help="Run the script without user interaction"
    )
    args = parser.parse_args()
    downloads_path: str = DOWNLOADS_PATH

    banners: Banner = Banner(args=args)
    banners.print_home()

    if not args.run_non_interactive:
        specific_folder = input("Welcome to the downloads organizer! Press enter to continue...\n")

        # This is an easter egg to allow the user to specify a folder within the downloads directory!
        if (
            specific_folder and
            os.path.exists(os.path.join(DOWNLOADS_PATH, specific_folder))
        ):
            downloads_path: str = os.path.join(DOWNLOADS_PATH, specific_folder)

    config: Config = Config(args=args)
    config.fetch_config()
    config.summarize_config()
    organizer = DownloadsOrganizer(
        downloads_path=downloads_path,
        config=config.config,
        args=args
    )
    organizer.organize_files()

    print("\n")
    banners.random_animal()

    if not args.run_non_interactive:
        input("Press enter to exit...")
