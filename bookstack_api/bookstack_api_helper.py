import sys

from bookstack_api.bookstack_api import BookStackAPI
from bookstack_api.api_url import *

class BookStackAPIHelper:

    def __init__(self, api: BookStackAPI):
        self.api = api
      
    def get_all(self, list_function, sort=None, filters=[]):
        all_records = []
        offset = 0
        total = sys.maxsize
        while len(all_records) < total:
            records_batch = list_function(offset=offset, count=500, sort=sort, filters=filters)
            all_records += records_batch['data']
            total = records_batch['total']
            offset += 500
        return all_records

    def get_all_pages(self, sort=None, filters=[]):    
        return self.get_all(self.api.pages.list, sort, filters)
    
    def get_all_books(self, sort=None, filters=[]):    
        return self.get_all(self.api.books.list, sort, filters)
    
    def get_all_shelves(self, sort=None, filters=[]):    
        return self.get_all(self.api.shelves.list, sort, filters)