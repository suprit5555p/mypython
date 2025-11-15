#encapsulation
class encap:
  def __init__(self): 
    self.public = 100
    self.__private = 10
  def function(self):
    print(self.__private) 
object=encap()
print(object.public) 
object.function() 
