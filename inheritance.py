#inheritance
class parents:
  def fun(self):
    print("i am good")
class child(parents):
  def fun(self):
    print("i am bad")
obj = parents()
pen = child()
obj.fun()
pen.fun()
