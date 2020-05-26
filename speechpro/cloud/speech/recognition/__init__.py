from speechpro.cloud.speech.recognition import rest
from speechpro.cloud.speech import common


class RecognitionClient(common.SpeechproApiClientBase, rest.ShortAudioRecognitionClient, rest.LongRunningRecognitionClient):
    pass


__all__ = ('RecognitionClient')