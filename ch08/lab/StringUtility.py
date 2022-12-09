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
      if s in ("aAeEiIoOuU a A e E i I o O u U"):
         count+= 1
      if count > 5:
         return ("many")
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
      return (self.string[0:2] + self.string[count - 2: count])
        

  def fixStart(self):
       '''
    general function: return a string where all occurrences of its first char have been changed to '*'
    args: self
    return:self.string
       '''
       for s in self.string:
        return self.string[0] + self.string[1:].replace(self.string[0], '*')


  #def asciiSum(self): Could not figure out

      
    #def cipher(self):  Could not figure out
      

    
    