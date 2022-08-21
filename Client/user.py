from enum import Enum


class State(Enum):
    LOBBY = 1
    ROOM_NOT_PLAYING = 2
    ROOM_PLAYING = 3


class User:

    def __init__(self):
        self.state = State.LOBBY

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state
