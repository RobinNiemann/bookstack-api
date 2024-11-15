class Filter:

    def __init__(self, key='', value='', operator=''):

        self.key = key
        self.value = value
        self.operator = operator

    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value
    
    def get_operator(self):
        return self.operator