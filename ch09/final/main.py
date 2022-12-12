import JokeAPI 
import YodaAPI 


def main():

  def showjoke(self):
    '''
  general function: To show the joke on the pygame screen and the shell
  args: self
  return: self
    '''
    num= JokeAPI.JokeAPI()
    jokes = num.get()
    for joke in jokes:
      text= (f"{joke['jokes']} Joke is:")
      print(text)

  def version(self):
    '''
  general function: Show the joke translated in Yoda on the pygame screen and the shell.
  args: self
  return: self
    '''
    var= YodaAPI.YodaAPI()
    translated = var.get()
    for yoda in translated:
      new= (f"{yoda[translated('text')]}, Joke in Yoda is: ")
      print(new)

main()