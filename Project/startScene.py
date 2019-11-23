from PyQt5.QtCore import QSize, QDir
from PyQt5.QtGui import QBrush, QFont, QPalette, QFontDatabase, QImage
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QPushButton, QLabel
from fonts import FontInitializer


class StartScene(QGraphicsScene):

    def __init__(self, parent, win_w, win_h):
        super().__init__(parent)
        self.win_w = win_w
        self.win_h = win_h
        FontInitializer()

        self.font = QFont(FontInitializer().miniPixel7)
        self.font.setPointSize(36)
        self.fontLabelAsteroids = QFont(FontInitializer().miniPixel7)
        self.fontLabelAsteroids.setPointSize(56)

        originalImage = QImage("imgs/asteroidStartScene.png")
        scaledImage = originalImage.scaled(QSize(800, 600))
        palette = QPalette()
        palette.setBrush(10, QBrush(scaledImage))
        self.setPalette(palette)
        self.setBackgroundBrush(palette.window())

        self.labelAsteroids = QLabel()
        self.labelAsteroids.setText("Asteroids")
        self.labelAsteroids.setStyleSheet("border:3px solid black;background:black;color:red;")
        self.labelAsteroids.setFont(self.fontLabelAsteroids)
        self.labelAsteroids.move(0, 10)
        self.addWidget(self.labelAsteroids)

        self.button2Players = QPushButton()
        self.button2Players.move(60, 150)
        self.button2Players.setText("2 players")
        self.button2Players.setFont(self.font)
        self.button2Players.setStyleSheet("border:1px solid black;background:black;color:yellow;")
        self.addWidget(self.button2Players)
        # self.button2Players.clicked().connect(.....)

        self.button3Players = QPushButton()
        self.button3Players.move(60, 250)
        self.button3Players.setText("3 players")
        self.button3Players.setFont(self.font)
        self.button3Players.setStyleSheet("border:1px solid black;background:black;color:yellow;")
        self.addWidget(self.button3Players)
        # self.button3Players.clicked().connect(.....)

        self.button4Players = QPushButton()
        self.button4Players.move(60, 350)
        self.button4Players.setText("4 players")
        self.button4Players.setFont(self.font)
        self.button4Players.setStyleSheet("border:1px solid black;background:black;color:yellow;")
        self.addWidget(self.button4Players)
        # self.button4Players.clicked().connect(.....)

