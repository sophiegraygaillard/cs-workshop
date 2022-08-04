class Person:
    def __init__(self, name):
      self.name = name
      self.friends = []

    def __str__(self):
      return("Hi! My name is {}".format(self.name))

    def addFriend(self, newFriend):
      self.friends.append(newFriend)

p = Person("jake")
p2 = Person("jayme")

print(p)
print(p2)

print(p.friends)
p.addFriend(p2)
print(p.friends[0].name)