import requests

class YodaAPI:
    '''
    general function: Creates the Yoda class by inserting the API link so that the text can be translated 
    args: self
    '''
    def __init__(self):
        self.api__url = f'https://api.funtranslations.com/translate/yoda.json'

    def get(self):
      '''
      general function: Uses the Yoda class to recieve data from the API specifically the translation feature
      args: self
      return: answer['translated']
      '''
      a = requests.get(self.api__url)
      answer = a.json()
      
      if answer.get('translated'):
            return answer['translated']
      else:
            return None
      
        
        
    
     

    
        