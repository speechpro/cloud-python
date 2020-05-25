import base64

from speechpro.cloud.speech.recognition.rest.cloud_client.api import RecognizeApi
from speechpro.cloud.speech.recognition.rest.cloud_client.models import AudioFileDto, RecognitionRequestDto

from speechpro.cloud.speech.recognition import enums

class ShortAudioRecognitionClient():

    model_mapping = {
        (enums.Language.RU, enums.Model.GENERAL): 'FarField',
        (enums.Language.RU, enums.Model.PHONE_CALL): 'TelecomRus',
        (enums.Language.KZ, enums.Model.PHONE_CALL): 'TelecomKz'
    }


    def recognize(self, config, audio):
        b64encoded_audio = base64.standard_b64encode(audio)
        audio_str = str(b64encoded_audio, 'ascii', 'ignore')

        recognize_api = RecognizeApi()
        audio_file = AudioFileDto(audio_str, config['encoding'].value)

        model = config['model'] if isinstance(config['model'], enums.Model) else enums.Model[config['model']]
        recognition_request = RecognitionRequestDto(
            audio_file, self.model_mapping[(config['language'], model)]
        )
        response_type = config.get('response_type')
        if response_type == enums.ResponseType.PLAIN_TEXT:
            return recognize_api.recognize(self.session_id, recognition_request)
        elif response_type == enums.ResponseType.WORD_LIST:
            return recognize_api.recognize_words(self.session_id, recognition_request)


class LongRunningRecognitionClient():
    pass