import requests

class JokeAPI:
    '''
    general function: Creates the Joke class by inserting the API link that will be used to distribute the programming jokes.
    args: self, amount, and type
    '''
    def __init__(self, amount=1, type = "single"):
        self.url = f'https://v2.jokeapi.dev/joke/Programming?type={type}&idRange=0-10&amount={amount}'

    def get(self):
      '''
      general function: Uses the Joke class to retrieve data from the API regarding the jokes
      args: self
      return: return response['jokes']
      '''
      r = requests.get(self.url)
      response = r.json()
      
      if response.get('jokes'):
            return response['jokes']
      else:
            return None
      
        
        
    
     

    
        