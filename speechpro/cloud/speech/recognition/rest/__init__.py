import base64

from speechpro.cloud.speech.recognition.rest.cloud_client.api import RecognizeApi
from speechpro.cloud.speech.recognition.rest.cloud_client.models import AudioFileDto, RecognitionRequestDto, AdvancedRecognitionRequestDto

from speechpro.cloud.speech.recognition import enums


CONFIG_MODEL_KEY = 'model'
CONFIG_LANGUAGE_KEY = 'language'


class ShortAudioRecognitionClient():

    model_mapping = {
        (enums.Language.RU, enums.Model.GENERAL): 'FarField',
        (enums.Language.RU, enums.Model.PHONE_CALL): 'TelecomRus',
        (enums.Language.KZ, enums.Model.PHONE_CALL): 'TelecomKz',
        (enums.Language.EN, enums.Model.PHONE_CALL): 'TelecomEngUs',
        (enums.Language.ES, enums.Model.PHONE_CALL): 'TelecomEsp'
    }

    def validate_enum_value(self, config, key, enum_type):
        try:
            return config[key] if isinstance(config[key], enum_type) else enum_type[config[key]]
        except:
            raise ValueError(f"{enum_type.__name__} is not provided or does not exist. Available models: {', '.join([m.name for m in enum_type])}")


    def recognize(self, config, audio):
        b64encoded_audio = base64.standard_b64encode(audio)
        audio_str = str(b64encoded_audio, 'ascii', 'ignore')

        recognize_api = RecognizeApi()
        audio_file = AudioFileDto(audio_str, config.get('encoding', enums.AudioEncoding.WAV).value)

        model = self.validate_enum_value(config, CONFIG_MODEL_KEY, enums.Model)
        language = self.validate_enum_value(config, CONFIG_LANGUAGE_KEY, enums.Language)
        mapped_model = self.model_mapping[(language, model)]

        recognition_request = RecognitionRequestDto(
            audio_file, mapped_model
        )
        response_type = config.get('response_type', enums.ResponseType.PLAIN_TEXT)
        if response_type == enums.ResponseType.PLAIN_TEXT:
            return recognize_api.recognize(self.session_id, recognition_request)
        elif response_type == enums.ResponseType.WORD_LIST:
            return recognize_api.recognize_words(self.session_id, recognition_request)
        elif response_type == enums.ResponseType.MULTICHANNEL:
            channel_count = config.get('audio_channel_count', 1)
            return recognize_api.recognize_advanced(
                self.session_id,
                AdvancedRecognitionRequestDto(
                    mapped_model, channels=[i for i in range(0, channel_count)], data=audio_str
                )
            )


class LongRunningRecognitionClient():
    pass