import time
#import uuid

class Animal:
  def __init__(self, name, type):
    self.id= time.strftime("%d%m%M%S")
    #self.id=self(id)
    #self.id=uuid()
    self.name = name
    self.type=type
    self.arrived=time.strftime("%d/%m/%Y")
    self.adopted= None

  def setadopted(self):
    self.arrived=time.strftime("%d/%m/%Y")

  def __str__():
    result_str = f"{self.name}"[{self.type}]"
    result_str += f"\narrived:{self.arrived}"
    result_str +=f"\nadopted:{self.adopted}"
    return result_str
    
def main():
  fido=Animal("fido", "cat")
  fido.set_adopted()
  print(fido)
  #a=Animal()
  #b=Animal()
main()