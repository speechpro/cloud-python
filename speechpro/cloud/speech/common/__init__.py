from speechpro.cloud.speech.common.rest.cloud_client.models.auth_status_dto import AuthStatusDto
from speechpro.cloud.speech.common.rest.cloud_client import SessionApi, AuthRequestDto


class SpeechproApiClientBase:
    def __init__(self, username, domain_id, password):
        self.username = username
        self.domain_id = domain_id
        self.password = password
        self._session_id = None


    def _check_session_status(self) -> bool:
        session_api = SessionApi()
        status: AuthStatusDto = session_api.check(self._session_id)
        return status.is_active


    @property
    def session_id(self):
        if self._session_id and self._check_session_status():
            return self._session_id
        else:
            session_api = SessionApi()
            credentials = AuthRequestDto(self.username, self.domain_id, self.password)
            self._session_id = session_api.login(credentials).session_id
            return self._session_id