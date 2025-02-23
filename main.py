import sys, os
if getattr(sys, '_MEIPASS', None):
    base_path = sys._MEIPASS
    ffmpeg_path = os.path.join(base_path, 'ffmpeg')
    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path
else:
    base_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_path)


# ----------------------------------------------------------------- #

from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QApplication()
window = MainWindow()
window.show()
app.exec()