class StringUtility:
  def __init__(self, string):
    self.string= string

  def __str__(self):
    '''
    general function: return the internal string itself, unchanged
    args: self
    return: self.string
    '''
    return self.string

  def vowels(self):
    '''
    general function: Count the number of vowels in the string, and return a new string of the form '<count>', where <count> is the number of vowels in the string as a string. But if the count is 5 or more, then  the loop returns the word 'many' instead of the actual count.
    args: self
    return: count
  
    '''
    count =0 
    for s in self.string:
      if s in ("aAeEiIoOuU"):
        count+= 1
      elif count>= 5:
        return("Many")
      else: 
        count=count
    return str(count)
 

    def bothEnds(self):
      '''
    general function: return a string made of the first 2 and last 2 chars of the original string
    args: self
    return: self.string
      '''
      count = 0
      
      for i in self.string:
        count = count +1
        return self.string[0:2] + self.string[-2]
        
        if self.string < 2:
           return ""
  

    def fixStart(self):
      '''
    general function: return a string where all occurrences of its first char have been changed to '*'
    args: self
    return:self.string
  
      '''
      str1 = str1.replace(self.string, '*')
      for s in self.string:
        return self.string[0] + str1[1: ]

        if self.string <= 1:
          self.string = self.string


    def asciiSum(self):
      '''
    general function: return an integer that is the sum of all ascii values in the string
    args: self
      '''
      num= sum(ord(self.string))
      print(num)
      

    #def cipher(self):
      

    
    