from bookstack_api.content_permissions import ContentPermissions
from bookstack_api.image_gallery import ImageGallery
from bookstack_api.shelves import Shelves
from bookstack_api.books import Books
from bookstack_api.pages import Pages
from bookstack_api.users import Users

class BookStackAPI:

    def __init__(self, base_url, token_id, token_secret):

        self.base_url = base_url
        self.token_id = token_id
        self.token_secret = token_secret
        self.shelves = Shelves(base_url, token_id, token_secret)
        self.books = Books(base_url, token_id, token_secret)
        self.pages = Pages(base_url, token_id, token_secret)
        self.content_permissions = ContentPermissions(base_url, token_id, token_secret)
        self.users = Users(base_url, token_id, token_secret)
        self.image_gallery = ImageGallery(base_url, token_id, token_secret)
        