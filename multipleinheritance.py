#multiple inheritance
class A:
  def fun1(self):
    print("day 1")
class B:
  def fun2(self):
    print("day 2")
class C(A,B):
  pass

obj1 = A()
obj2 = B()
obj1.fun1()
obj2.fun2()
