import requests
from bookstack_api.url_builder import create_url_parameters_string

class ImageGallery:
    
    def __init__(self, base_url, token_id, token_secret):
        self.base_url = base_url
        self.token_id = token_id
        self.token_secret = token_secret


    def read(self, id):
        api_url = (self.base_url + '/image-gallery/' + str(id))
        response = requests.get(api_url, headers={'Authorization': 'Token {0}:{1}'.format(self.token_id, self.token_secret)})
        response.raise_for_status()
        return response.json()
    
    
    def list(self, count=0, offset=0, sort=None, filters=[]):
        api_url = self.base_url + '/image-gallery?' + create_url_parameters_string(count, offset, sort, filters)
        response = requests.get(api_url, headers={'Authorization': 'Token {0}:{1}'.format(self.token_id, self.token_secret)})
        response.raise_for_status()
        return response.json()


    def create(self, body):
        api_url = self.base_url + '/image-gallery'
        response = requests.post(api_url, json=body, headers={'Authorization': 'Token {0}:{1}'.format(self.token_id, self.token_secret)})
        response.raise_for_status()
        return response.json()