import requests
from common import config
from lxml import html
class Parser:
    def __init__(self, site):
        self._page = None
        self._site = site
        
    
    def parse(self):
        if self._page is None:
            response = requests.get(config()["sites"][self._site]["url"])
            content = response.content.decode("utf-8")
            if response.status_code == 200:
                self._page = html.fromstring(content)
            else:
                raise ValueError(f"Response error: {response.status_code}")
        return self
    
    def __str__(self):
        return f"last search: {self._site}"
    
    def __repr__(self):
        return "Parser {%s}" % self
    
    @property
    def page(self):
        return self._page
    
    
    @property
    def last_seach_pattern(self):
        return self._pattern
    
    
    def extract(self, pattern):
        self.__pattern = pattern
        res = None
        if self.page is not None:
            res = self._page.xpath(pattern)
        return res
    
        

class Home(Parser):

    def __init__(self, site):
        super().__init__(site)
        
    @property
    def links(self):
        if self.page is not None:
            links = self.extract(config()["sites"][self._site]["links"])
        else:
            raise Exception("you need parsing the site")
        return links
    

class Article(Parser):

    def __init__(self, site):
        self._path = None
        self.url = None
        super().__init__(site)
    
    def set_path(self,path):
        self._page = None
        self._path = path
        
    def parse(self):
        if  self._page is None and self._path is not None:
            self.url = config()["sites"][self._site]["url"] + self._path
            response = requests.get(self.url)
            content = response.content.decode("utf-8")
            if response.status_code == 200:
                self._page = html.fromstring(content)
            else:
                raise ValueError(f"Response error: {response.status_code}")
        elif self._path is None:
            raise NameError(f"pagina: {self._page}")
        return self

        
    
    @property
    def date(self):
        return self.extract(config()['sites'][self._site]['article']['date'])[0]

    @property
    def body(self):
        corpus = self.extract(config()['sites'][self._site]['article']['body'])
        return "\n".join(corpus).strip()

    @property
    def resumen(self):
        res = self.extract(config()['sites'][self._site]['article']['resumen'])
        return "".join(res).strip()


    @property
    def title(self):
        title = self.extract(config()['sites'][self._site]['article']['header'])
        return "\n".join(title).strip()


    





