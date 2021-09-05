from prettyconf import config


class Settings:
    INPUT_DIR = config("INPUT_DIR")
    OUT_DIR = config("OUT_DIR")


settings = Settings()
