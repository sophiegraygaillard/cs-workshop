class Player:
  def __init__(self, name, symbol):
    self.name = name
    self.symbol = symbol

  def __str__(self):
    return("Player {} ({})".format(self.name, self.symbol))

class Board:
  emptySpace = "."
  size = 3

  def __init__(self):
    self.board = [[self.emptySpace] * 3 for i in range(0, self.size)]

  def __str__(self):
    strRepresent = ["".join(x) for x in self.board]
    strRepresent = "\n".join(strRepresent)

    return(strRepresent)

  def checkVicotry(self, player):
    sym = player.symbol
    successList = [sym] * self.size

    # diagonal check
    topLeftToBottomRight = [self.board[i][i] for i in range(0, self.size)]
    bottomLeftToTopRight = [self.board[i][2-i] for i in range(0, self.size)]

    diagonalPass = topLeftToBottomRight == successList or bottomLeftToTopRight == successList
    
    if diagonalPass:
      return(True)

    # row check
    for row in self.board:
      if row == successList:
        return(True)

    # col check
    for i in range(0, self.size):
      col = [self.board[row][i] for row in range(0, self.size)]
      if col == successList:
        return(True)

    return(False)

  def markBoard(self, player, coord):
    row = coord[0]
    col = coord[1]

    if row < 0 or row >= self.size:
      print("Row coordinate out of bounds.")
      return(None)
    elif col < 0 or col >= self.size:
      print("Col coordinate out of bounds.")
      return(None)

    if self.board[row][col] != self.emptySpace:
      print("Current coordinate has already been played. Try again.")
      return(None)

    self.board[row][col] = player.symbol
    return(self.checkVicotry(player))


def createPlayer(playerNum, symbol):
  name = input("Player {}, you will be {}. Please enter your name: ".format(playerNum, symbol))
  p = Player(name, symbol)
  return(p)


def promptPlayerTurn(player, board):
  successfulTurn = False

  while not successfulTurn:
    coord = input("Player {}, please enter coordinates (i.e. 0,2): ".format(player.name))

    coordList = coord.split(",")
    if len(coordList) != 2:
      print("Coordinate nomenclature not correct. Try again.\n")
      continue

    try:
      coordList = [int(x) for x in coordList]
      check = board.markBoard(player, coordList)

      if check is not None:
        successfulTurn = True
        return(check)

    except ValueError:
      print("Coordinate input was not an integer. Try again.\n")


def main():
  p1 = createPlayer(1, "X")
  p2 = createPlayer(2, "O")

  gameBoard = Board()

  print("Welcome to tic tac toe, {} and {}.".format(p1, p2))
  print("This is the current board.")
  print(gameBoard)

  gameFinished = False
  while not gameFinished:
    p1Turn = promptPlayerTurn(p1, gameBoard)
    print(gameBoard)

    if p1Turn:
      print("Game finished. Player {} wins.".format(p1.name))
      gameFinished = True
      continue

    p2Turn = promptPlayerTurn(p2, gameBoard)
    print(gameBoard)

    if p2Turn:
      print("Game finished. Player {} wins.".formt(p2.name))
      gameFinished = True
      continue


main()