from speechpro.cloud.speech.synthesis import rest
from speechpro.cloud.speech import common
from speechpro.cloud.speech.synthesis import enums

class SynthesisClient(common.SpeechproApiClientBase, rest.BatchSynthesisClient):
    pass


__all__ = ('SynthesisClient', 'enums')