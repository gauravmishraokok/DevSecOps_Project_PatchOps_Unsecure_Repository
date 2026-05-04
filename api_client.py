import search_engine

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_catalog(self):
        return search_engine.execute_search("")
