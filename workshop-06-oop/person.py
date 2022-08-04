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
    return("HIiiiiiiiiiiii! My name is {}".format(self.name))


p = Person("Betina")
p2 = Person("Alban")

print(p)

coolP = AVeryCoolPerson("Baloo")
print(coolP)
