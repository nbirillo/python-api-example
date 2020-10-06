# Copyright (c) 2020 Anastasiia Birillo

import os
from typing import Optional

import dotenv
import requests
from requests import Response

from src.main.python.vk_user import VkUser


class BaseApiHandler:
    _ERROR_KEY: str = 'error'
    _RESPONSE_KEY: str = 'response'

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    def execute_get_query(self, url: str, params: Optional[dict] = None) -> Optional[dict]:
        url = f'{self._base_url}/{url}'
        print(f'Executing GET query. Current url is {url}. Current params are {params}')
        response = requests.get(url, params=params)
        if not self.is_successful(response):
            print(f'The error code is: {response.status_code}')
            return None
        print(f'The query was executed successful')
        return response.json()[self._RESPONSE_KEY]

    @classmethod
    def is_successful(cls, response: Response) -> bool:
        return response.status_code == requests.codes.ok and response.json().get(cls._ERROR_KEY) is None


class VkApiHandler(BaseApiHandler):
    def __init__(self) -> None:
        super().__init__('https://api.vk.com')
        dotenv.load_dotenv()
        self._version = '5.70'
        # https://vk.com/dev/authcode_flow_user
        self._token = os.getenv('TOKEN')
        # https://vk.com/apps?act=manage
        self._service_key = os.getenv('SERVICE_KEY')

    def _get_base_params(self) -> dict:
        return {
            'access_token': self._token,
            'v': self._version
        }

    # https://vk.com/dev/users.get
    def get_current_user(self) -> Optional[VkUser]:
        return self.get_user_by_id()

    def get_user_by_id(self, id: Optional[int]=None) -> Optional[VkUser]:
        params = self._get_base_params()
        params['fields'] = "sex,about,city,domain,education,career"
        params['user_ids'] = id
        url = 'method/users.get'
        response = self.execute_get_query(url, params)
        if response is not None:
            return VkUser(response[0])
        return response
