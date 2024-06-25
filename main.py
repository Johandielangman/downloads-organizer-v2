import argparse
import os

from utils.organizer import DownloadsOrganizer
from utils.config import Config
from utils.style import Banner
from colorama import (
    init,
    Fore,
    Back,
    Style
)
from constants import (
    DOWNLOADS_PATH
)

if __name__ == "__main__":

    init(autoreset=True)
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
        specific_folder = input("Welcome to the downloads organizer! " + Fore.GREEN + "Press enter to continue...\n")

        # This is an easter egg to allow the user to specify a folder within the downloads directory!
        if (
            specific_folder and
            os.path.exists(os.path.join(DOWNLOADS_PATH, specific_folder))
        ):
            downloads_path: str = os.path.join(DOWNLOADS_PATH, specific_folder)

    # check to make sure that this file is not in the downloads folder
    if downloads_path == os.path.dirname(os.path.realpath(__file__)):
        print(Fore.RED + "Oops! " + Fore.WHITE + "Please move this file out of the downloads folder before running the script. We don't want to organize ourselves! \n")
        input(Fore.GREEN + "Press enter to exit...")
        exit(1)

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
