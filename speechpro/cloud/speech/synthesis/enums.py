import enum

class Voice(enum.Enum):
    ANNA = 1
    JULIA = 2
    VLADIMIR = 3


class PlaybackProfile(enum.Enum):
    SPEAKER = 1
    PHONE_CALL = 2