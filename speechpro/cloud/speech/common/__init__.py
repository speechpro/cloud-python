from typing import Optional, Union
import os

import toml
from speechpro.cloud.speech.common.rest.cloud_client.models.auth_status_dto import AuthStatusDto
from speechpro.cloud.speech.common.rest.cloud_client import SessionApi, AuthRequestDto


class SpeechproApiClientBase:
    def __init__(self, username: Optional[str] = None, domain_id: Optional[Union[str, int]] = None, password: Optional[str] = None):
        if username and domain_id and password:
            self.username = username
            self.domain_id = domain_id
            self.password = password
        else:
            profile: str = os.environ.get('SPEECHPRO_PROFILE', 'default')
            try:
                f = os.path.expanduser(os.path.join('~', '.speechpro', 'credentials'))
                credentials = toml.load(f)[profile]
                self.username = credentials['username']
                self.domain_id = credentials['domain_id']
                self.password = credentials['password']
            except (FileNotFoundError, KeyError):
                self.username = os.environ.get('SPEECHPRO_USERNAME')
                self.domain_id = os.environ.get('SPEECHPRO_DOMAIN_ID')
                self.password = os.environ.get('SPEECHPRO_PASSWORD')

        self._session_id = None


    def _check_session_status(self) -> bool:
        session_api = SessionApi()
        status: AuthStatusDto = session_api.check(self._session_id)
        return status.is_active


    @property
    def session_id(self) -> str:
        if self._session_id and self._check_session_status():
            return self._session_id
        else:
            session_api = SessionApi()
            credentials = AuthRequestDto(self.username, self.domain_id, self.password)
            self._session_id = session_api.login(credentials).session_id
            return self._session_id