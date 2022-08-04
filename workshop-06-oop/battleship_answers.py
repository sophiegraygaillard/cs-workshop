from random import randint

class Ship:
  def __init__(self, size, orient, location):
    self.size = size
    self.orient = orient
    self.location = location

    self.hp = size
    
  def __str__(self):
    return("Ship ({})".format(self.size))

  def takeDamage(self):
    self.hp = self.hp - 1

    return(self.hp == 0)


class Board:
  def __init__(self, private = True, size = 10):
    self.size = size
    self.board = [["o"] * self.size for i in range(0, size)]
    self.private = private
    self.ships = []
    self.sunkenShips = []

    if self.private:
      self.shipLocations = {}

    # o is empty space
    # | or - is ship position
    # x is confirmed strike
    # n is confirmed open space

  def __str__(self):
    buffer = " " * 5

    strRepresent = [str(index) + ") " + buffer.join(x) for index, x in enumerate(self.board)]
    strRepresent = "\n".join(strRepresent)

    prefixBuffer = " " * 3
    colCoordinates = prefixBuffer + buffer.join([str(i) for i in range(0, self.size)])
    colSeparator = "~" * len(colCoordinates)

    strRepresent = "\n" + colCoordinates + "\n" + colSeparator + "\n" + strRepresent + "\n"

    return(strRepresent)

  def allShipsSunk(self):
    return(len(self.sunkenShips) == len(self.ships))

  def addShip(self, ship):
    row = ship.location[0]
    col = ship.location[1]
    
    # check if row and col are within bounds
    if row < 0 or col < 0 or row >= self.size or col >= self.size:
      print("Coordinate location is out of bounds.")
      return(False)

    # check if location is free
    if self.board[row][col] != "o":
      print("Coordinate is not an open space.")
      return(False)

    # check orientation and adjacent spaces
    if ship.orient ==  "V" and ship.size + row <= self.size:
      self.ships.append(ship)

      for i in range(0, ship.size):
        self.board[row + i][col] = "|"
        self.shipLocations[str([row + i, col])] = {"ship": ship, "hit": False}

    elif ship.orient == "H" and ship.size + col <= self.size:
      self.ships.append(ship)

      for i in range(0, ship.size):
        self.board[row][col + i] = "-"
        self.shipLocations[str([row, col + i])] = {"ship": ship, "hit": False}

    else:
      print("Ship will not fit in board with current orientation and location")
      return(False)
    
    print("{} added to board with orientation {} and location: {}.\n".format(ship, ship.orient, ship.location))
    return(True)


  def markMissile(self, location, markAttackBoard = False, attackSuccess = None):
    row = location[0]
    col = location[1]

    if markAttackBoard and attackSuccess:
      self.board[row][col] = "x"
      return(True)

    elif markAttackBoard and not attackSuccess:
      self.board[row][col] = "n"
      return(False)

    if row >= self.size or col >= self.size:
      print("Error: firing location not valid.")
      return(None)

    if self.private:
      coord = str([row, col])
      if coord in self.shipLocations:
        shipInfo = self.shipLocations[coord]
        ship = shipInfo["ship"]
        shipHit = shipInfo["hit"]

        if shipHit:
          print("Already a confirmed missile hit.\n")
          return(True)

        print("Confirmed missile hit.\n")
        result = ship.takeDamage()
        shipInfo["hit"] = True

        if result:
          print("{} has been destroyed.\n".format(ship))
          self.sunkenShips.append(ship)

        self.board[row][col] = "x"  
        return(True)

    print("Miss.\n")
    self.board[row][col] = "n"
    return(False)


class Player:
  def __init__(self, name, privateBoard, targetBoard):
    self.name = name
    self.privateBoard = privateBoard
    self.targetBoard = targetBoard


def createPlayer(namePrompt, debug = False):
  if debug:
    p = Player(str(randint(0, 5)), Board(private=True), Board(private=False))
    # ships = [
    #   Ship(5, "V", [3, 1]),
    #   Ship(4, "H", [3, 2]),
    #   Ship(3, "H", [7, 7]),
    #   Ship(3, "H", [7, 2]),
    #   Ship(2, "V", [0, 0])]

    ships = [Ship(2, "V", [0, 0])]
    for s in ships:
      p.privateBoard.addShip(s)

    return(p)

  pName = input(namePrompt)
  p = Player(pName, Board(private=True), Board(private=False))

  shipSizes = [5, 4, 3, 3, 2]
  index = 0
  while index < len(shipSizes):
    shipInput = input("Please input ship (" + str(shipSizes[index]) + ") ship orientation,row,column (i.e. V,3,5 or H,0,9): ")
    shipInputList = shipInput.split(",")
    
    if len(shipInputList) != 3:
      print("Incorrect nomenclature. Please try again.")
      continue

    try:
      shipInputCoord = [int(i) for i in shipInputList[1:3]]
    except ValueError:
      print("Incorrect nomenclature for input. Requires integer value.")
      continue
    
    ship = Ship(shipSizes[index], shipInputList[0], shipInputCoord)
    check = p.privateBoard.addShip(ship)
    
    if check:
      index += 1

  return(p)


def promptMissile(attacker: Player, defender: Player):
  successCoordInput = False
  message = "Player {}'s turn. Please enter coordinates for missile (i.e. 3,5 or 0,2).\nTo check your own boards: type !showMyBoard or !showMyFiredMissiles : "

  while not successCoordInput:
    coordInput = input(message.format(attacker.name))

    if coordInput == "!showMyBoard":
      print(attacker.privateBoard)
      continue
    elif coordInput == "!showMyFiredMissiles":
      print(attacker.targetBoard)
      continue

    coordInputList = coordInput.split(",")

    if len(coordInputList) != 2:
      print("Coordinate nomenclature not correct. Try again.\n")
      continue

    try:
      coordInputList = [int(x) for x in coordInputList]
      check = defender.privateBoard.markMissile(coordInputList)

      if check is not None:
        attacker.targetBoard.markMissile(coordInputList, markAttackBoard = True, attackSuccess = check)
        successCoordInput = True

    except ValueError:
      print("Coordinate input was not an integer. Try again.\n")


def main():
  p1 = createPlayer("Player 1 name: ", debug = False)
  p2 = createPlayer("Player 2 name: ", debug = False)

  gameFinished = False
  while not gameFinished:
    promptMissile(p1, p2)
    if p2.privateBoard.allShipsSunk():
      print("Game finished. Player {} wins.".format(p1.name))
      gameFinished = True
      continue

    promptMissile(p2, p1)
    if p1.privateBoard.allShipsSunk():
      print("Game finished. Player {} wins.".formt(p2.name))
      gameFinished = True
      continue


main()