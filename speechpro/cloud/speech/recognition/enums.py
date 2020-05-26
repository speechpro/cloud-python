import enum


class AudioEncoding(enum.Enum):
    WAV = 'audio/wav'
    OGG_OPUS = 'audio/ogg'


class Model(enum.IntEnum):
    GENERAL = 1
    PHONE_CALL = 2


class Language(enum.IntEnum):
    RU = 1
    EN = 2
    ES = 3
    KZ = 4


class ResponseType(enum.Enum):
    PLAIN_TEXT = 'plaintext'
    WORD_LIST = 'wordlist'
    MULTICHANNEL = 'multichannel'