from speechpro.cloud.speech.common.rest.cloud_client import SessionApi, AuthRequestDto


class SpeechproApiClientBase:
    def __init__(self, username, domain_id, password):
        self.username = username
        self.domain_id = domain_id
        self.password = password
        self._session_id = None


    @property
    def session_id(self):
        if not self._session_id:
            session_api = SessionApi()
            credentials = AuthRequestDto(self.username, self.domain_id, self.password)
            self._session_id = session_api.login(credentials).session_id
        return self._session_id