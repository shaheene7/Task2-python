class Cache:
    
    def get(self, key):
        pass

class DB:
    
    def get(self, table):
        pass


class API:

  def call(self):
      pass


class Facade:
   
   def __init__(self):
       self._cache = Cache()
       self._db = DB()
       self._api = API()

   @property
   def cache(self):
       return self._cache
   
   @property
   def db(self):
       return self._db
   
   @property
   def api(self):
       return self._api
   
   def start(self):
       self._cache.get("key")
       self._db.get("table")
       self._api.call()

 
facade = Facade()
facade.start()



""" it provides a simple, unified interface to a set of complex subsystems, 
    making common tasks easier for most users"""