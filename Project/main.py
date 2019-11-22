import sys

from PyQt5.QtWidgets import QApplication, QGraphicsView

from scenes import SceneState


class MainWindow(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asteroid")
        self.win_w = 850
        self.win_h = 650
        self.rect().center()
        self.setFixedWidth(self.win_w)
        self.setFixedHeight(self.win_h)
        self.sceneState = SceneState.NONE
        # self.setScene(CUSTOM_SCENE)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    mw = MainWindow()
    sys.exit(app.exec_())
