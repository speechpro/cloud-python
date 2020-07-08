import base64

from speechpro.cloud.speech.synthesis.rest.cloud_client import Synthesize, SynthesizeRequest, SynthesizeText
from speechpro.cloud.speech.synthesis import enums

class BatchSynthesisClient:
    voice_profile_mapping = {
        (enums.Voice.VLADIMIR, enums.PlaybackProfile.SPEAKER): 'Vladimir_n',
        (enums.Voice.VLADIMIR, enums.PlaybackProfile.PHONE_CALL): 'Vladimir_8000n',
        (enums.Voice.ANNA, enums.PlaybackProfile.SPEAKER): 'Anna_n',
        (enums.Voice.ANNA, enums.PlaybackProfile.PHONE_CALL): 'Anna_8000n',
        (enums.Voice.JULIA, enums.PlaybackProfile.SPEAKER): 'Julia_n',
        (enums.Voice.JULIA, enums.PlaybackProfile.PHONE_CALL): 'Julia_8000n',
        (enums.Voice.DASHA, enums.PlaybackProfile.SPEAKER): 'Dasha_n',
        (enums.Voice.DASHA, enums.PlaybackProfile.PHONE_CALL): 'Dasha_8000n',
        (enums.Voice.ASEL, enums.PlaybackProfile.SPEAKER): 'Asel_n',
        (enums.Voice.ASEL, enums.PlaybackProfile.PHONE_CALL): 'Asel_8000n',
        (enums.Voice.CAROL, enums.PlaybackProfile.SPEAKER): 'Carol_n',
        (enums.Voice.CAROL, enums.PlaybackProfile.PHONE_CALL): 'Carol_8000n',
    }


    def get_enum_value(self, value, enum_type):
        return value if isinstance(value, enum_type) else enum_type[value]


    def synthesize(self, voice, profile, text):
        try:
            voice = self.get_enum_value(voice, enums.Voice)
            profile = self.get_enum_value(profile, enums.PlaybackProfile)
            mapped_voice = self.voice_profile_mapping[(voice, profile)]
        except KeyError:
            raise ValueError('Incorrect combination of voice and playback profile')
        synthesize = Synthesize()
        text_request = SynthesizeText("text/plain", text)
        synthesize_request = SynthesizeRequest(text_request, mapped_voice, "audio/wav")
        audio_data = synthesize.synthesize(self.session_id, synthesize_request)
        sound = base64.decodebytes(bytes(audio_data.data, 'utf-8'))

        return sound