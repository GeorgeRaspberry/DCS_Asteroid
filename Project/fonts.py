from PyQt5.QtCore import QDir
from PyQt5.QtGui import QFontDatabase


class FontInitializer:

    def __init__(self):
        dir_ = QDir("fonts")
        _id = QFontDatabase.addApplicationFont("fonts/mini_pixel-7.ttf")
        self.miniPixel7 = QFontDatabase.applicationFontFamilies(_id)[0]
