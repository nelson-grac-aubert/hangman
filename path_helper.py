import os, sys

def resource_path(relative_path):
    """ Returns the absolute path to an asset for pyinstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)