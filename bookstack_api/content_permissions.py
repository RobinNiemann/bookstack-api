
from typing import Literal

import requests


class ContentPermissions:
    
    def __init__(self, base_url, token_id, token_secret):
        self.base_url = base_url
        self.token_id = token_id
        self.token_secret = token_secret
    
    
    def read(self, content_type: Literal['page', 'book', 'chapter', 'bookshelf'], content_id: int|str):
        api_url = self.base_url + '/content-permissions/' + content_type + '/' + str(content_id)
        response = requests.get(api_url, headers={'Authorization': 'Token {0}:{1}'.format(self.token_id, self.token_secret)})
        response.raise_for_status()
        return response.json()
    
    
    def update(self, content_type: Literal['page', 'book', 'chapter', 'bookshelf'], content_id: int|str, body=None):
        api_url = self.base_url + '/content-permissions/' + content_type + '/' + str(content_id)
        response = requests.put(api_url, json=body, headers={'Authorization': 'Token {0}:{1}'.format(self.token_id, self.token_secret)})
        response.raise_for_status()
        return response.json()