#polymorphisum
class gokak:
  def arith(self, a, b):
    return a+b
class belagavi(gokak):
  def arith(self, a, b):
    return a-b
obj1 = gokak()
obj2 = belagavi()
print(obj1.arith(10,20))
obj2.arith(10,20)
