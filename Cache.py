import requests #using requests
import json #using json


class cache():

def __init__(self, string, ttl=30, cache_name='cache', backend=None, expire_after=60, 
                 , allowable_methods=('GET', 'POST'), #Has GET and POST
                 old_data_on_error=False, ):
    self.string = string
    self.expires_at = time() + ttl #Expires after ttl
    self._expired = True
	 expire_after = timedelta(seconds=expire_after)
     self._cache_expire_after = expire_after

  def expired(self):
    if self._expired is False:
      return (self.expires_at < time())
    else:
      return self._expired
	if self._expired is True:
      return (clear.cache)

	  
class CacheList():

  def add_entry(self, string, ttl=30):
   self.data = {"id" : int, "message" : string } #adding data json
	  


if __name__ == '__main__':

	response = requests.post(url, self.data=self.data, json={'json_payload': self.data} #posting the data
	
	response = requests.get('https://url', self.data) # gets the data in cache
	cache.remove(self.data) #clears cache
	print data["id"]{"message"]
