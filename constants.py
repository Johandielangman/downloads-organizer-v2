import os

USER_DIRECTORY = os.path.expanduser("~")  # This will get the path of the user's directory
DOWNLOADS_PATH = os.path.join(USER_DIRECTORY, "Downloads")

# These are a few good default folders to have
DOWNLOAD_FOLDERS = {
    "Images": ["png", "jpeg", "jpg", "svg", "webp", "ico", "drawio"],
    "PowerPoints": ["pptx", "ppt"],
    "Spreadsheets": ["xlsx", "xls", "csv"],
    "Documents": ["docx", "doc", "pdf", "txt", "md", "html"],
    "Archive Files": ["zip", "rar", "7z"],
    "Videos": ["mp4", "gif"],
    "Music": ["mp3"],
    "LaTex": ["tex"],
    "Executable": ["exe", "msi"],
    "Programming": ["py", "json", "db", "yml", "yaml"],
    "Outlook": ["msg"],
}
UNCATOGORIZED_FOLDER = "Uncatogorized"
OTHER_DOWNLOADS_FOLDER = "Others"
EXCEL_FILE_NAME = "Downloads Organizer Config.xlsx"
EXCEL_SHEET_NAME = "Config"