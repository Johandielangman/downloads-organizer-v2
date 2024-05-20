from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

import os
from constants import (
    EXCEL_FILE_NAME,
    DOWNLOAD_FOLDERS
)


class ConfigBuilder:
    def __init__(self) -> None:
        self.n_rows = 0
        self.n_cols = 0

    def new_workbook(self) -> Workbook:
        wb = Workbook()
        ws = wb.active
        ws.title = "Config"
        return wb

    def add_config_header(self, ws: Workbook) -> None:
        headers = ["Folder Name", "Extension"]
        self.n_cols = len(headers)
        ws.append(headers)

    def add_config_rows(self, ws: Workbook) -> None:
        for folder_name, extensions in DOWNLOAD_FOLDERS.items():
            for extension in extensions:
                ws.append([folder_name, extension])
                self.n_rows += 1

    def get_ref_table(self, ws: Workbook) -> str:
        return f"A1:{chr(65 + self.n_cols - 1)}{self.n_rows + 1}"

    def create_table(self, ws: Workbook) -> None:
        ref = self.get_ref_table(ws)
        tab = Table(displayName="ConfigTable", ref=ref)
        style = TableStyleInfo(
            name="TableStyleMedium9",
            showFirstColumn=False,
            showLastColumn=False,
            showRowStripes=True,
            showColumnStripes=True
        )
        tab.tableStyleInfo = style
        ws.add_table(tab)

    def save_table(self, wb: Workbook) -> None:
        print(f"Saving config file: {EXCEL_FILE_NAME}")
        wb.save(EXCEL_FILE_NAME)

    def create_config_file(self) -> None:
        wb: Workbook = self.new_workbook()
        ws = wb["Config"]

        self.add_config_header(ws)
        self.add_config_rows(ws)
        self.create_table(ws)
        self.save_table(wb)


class Config(ConfigBuilder):
    def __init__(self) -> None:
        super().__init__()

    def does_config_file_exist(self) -> bool:
        return os.path.exists(os.path.join(os.getcwd(), EXCEL_FILE_NAME))

    def get_config(self) -> dict:
        config = {}
        if not self.does_config_file_exist():
            response: str = input("Config file does not exist. Do you want to create it? (y/n): ")
            if response.lower() == "y":
                self.create_config_file()
                return DOWNLOAD_FOLDERS
            else:
                exit()
        else:
            print(f"Found the '{EXCEL_FILE_NAME}' file. Reading config...")
            self.read_config_file(config)
        return config

    def clean_config_file(self, config: dict) -> None:
        for folder_name, extensions in config.items():
            extensions = [ext.lower() for ext in extensions]
            config[folder_name] = list(set(extensions))

    def read_config_file(self, config: dict) -> dict:
        wb = load_workbook(EXCEL_FILE_NAME)
        ws = wb["Config"]

        for row in ws.iter_rows(min_row=2, values_only=True):
            folder_name, extension = row
            if folder_name not in config:
                config[folder_name] = [extension]
            else:
                config[folder_name].append(extension)

        self.clean_config_file(config)
        return config
