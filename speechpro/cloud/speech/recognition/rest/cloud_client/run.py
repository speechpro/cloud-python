import base64
import cloud_client
from speechpro.cloud.speech.recognition.rest.cloud_client.models.auth_request_dto import AuthRequestDto
from speechpro.cloud.speech.recognition.rest.cloud_client.api.session_api import SessionApi
from speechpro.cloud.speech.recognition.rest.cloud_client.api import PackagesApi
from speechpro.cloud.speech.recognition.rest.cloud_client.api import RecognizeApi
from speechpro.cloud.speech.recognition.rest.cloud_client.models.audio_file_dto import AudioFileDto
from speechpro.cloud.speech.recognition.rest.cloud_client.models.recognition_request_dto import RecognitionRequestDto

session_api = SessionApi()
credentials = AuthRequestDto("kozhedubov@speechpro.com", 863, "bb1e439bY#")
session_id = session_api.login(credentials).session_id
packages_api = PackagesApi()
packages_api.load(session_id, "FarField").status
in_file = open("~/documents/Projects/STC/CP/stafory/sample_1.wav", "rb")
data = in_file.read()
in_file.close()
encoded_string = base64.standard_b64encode(data)
string = str(encoded_string, 'ascii', 'ignore')
recognize_api = RecognizeApi()
audio_file = AudioFileDto(string, "audio/x-wav")
recognition_request = RecognitionRequestDto(audio_file, "FarField")
recognition_result = recognize_api.recognize(session_id, recognition_request)
print(recognition_result)
