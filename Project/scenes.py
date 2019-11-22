from enum import Enum

""" For scene dimensions use self.setSceneRect(QRectF(0, 0, self.win_w - 50, self.win_h - 50))"""


class SceneState(Enum):
    NONE = 0,
    START_SCENE = 1,
    GAME_SCENE = 2,
    END_SCENE = 3
