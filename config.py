from prettyconf import config


class Settings:
    READ_PDFS_FROM_FOLDER = config("PDFS_FOLDER")
    EXPORT_CSV_TO_FOLDER = config("EXPORT_CSV_TO_FOLDER")
