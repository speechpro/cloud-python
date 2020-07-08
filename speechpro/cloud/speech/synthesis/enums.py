import enum

class Voice(enum.Enum):
    ANNA = 1
    JULIA = 2
    VLADIMIR = 3
    DASHA = 4
    ASEL = 5
    CAROL = 6


class PlaybackProfile(enum.Enum):
    SPEAKER = 1
    PHONE_CALL = 2