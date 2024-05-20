import os

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
EXCEL_FILE_NAME = "Downloads Organizer Config.xlsx"