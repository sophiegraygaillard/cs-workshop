class Person:
  def __init__(self, name):
    self.name = name
    self.friends = []

  def __str__(self):
    return("Hi! My name is {}".format(self.name))

  def addFriends(self, newFriends):
    if isinstance(newFriends, list):
      self.friends = self.friends + newFriends
    else:
      self.friends.append(newFriends)


class AVeryCoolPerson(Person):
  def __str__(self):
    return("Hiiiiiiiiiiii! My name is {}".format(self.name))


p = Person("bob")
p.addFriends("hi3")
p.addFriends(["hi", "hi2"])
print(p.friends)

vp = AVeryCoolPerson("bobber")
print(vp.friends)