# workshop-06 homework - Battleship!

Welcome to the homework for workshop-06. You will be using what you've learned in class about object-oriented programming to build an interactive terminal-based game of Battleship.

## How this game works
Two players play this game. Each player has an armada consisting of 5 ships with the following sizes: 5, 4, 3, 3, 2.

Each player has two boards:
1. The first board is a private board where the players place their ships in a 10x10 grid without any overlap. Ships may only be placed in vertical or horizontal orientations.
2. The second board is where the player's missile shots (whether they were confirmed hits or misses) are reported.

Game progression:
1. Player 1 places their armada
2. Player 2 places their armada
3. Player 1 begins by guessing a coordinate location. If the corresponding location on Player 2's board contains a ship, Player 2 will report that there was a confirmed missile hit. Otherwise, Player 2 will report that the shot was a miss. If a hit is confirmed and an entire ship has sunk, the target Player will also need to report that the ship has sunk.
4. Player 2 then fires a missile and Player 1 will report whether it was a hit or miss.
5. Repeat Steps 3 and 4 until any player has lost all their ships, thus crowning the survivor as the winner.

## The requirements
You will need to build the following objects. No inheritance is needed for this entire project.
- Ship
- Board
- Player

For the `Ship` object:
- Needs to be able to created with the following information:
  - the size of the ship.
  - the orientation
  - the coordinate location (i.e. if the ship size was 2; orientation was vertical; coordinate was 0,0, then the ship would be at 0,0 and 1,0)

For the `Board` object:
  - Will contain several attributes including (but not excluding):
    - A 10x10 grid represented by a nested list. Each sub element will be a character as such:
      - `o` is empty space
      - `|` or `-` is ship position depending on if vertical or horizontal, reespectively
      - `x` is confirmed strike
      - `n` is confirmed open space

For the `Player` object:
- Needs to be able to created with the following information:
  - their name
  - their private `Board` (this will record this player's ship and received missiles)
  - their target `Board` (this will record this player has fired missiles)


Other requirements:
- As this game requires input from users, your code should be designed to check for errors in input.
- Players need to be able to check their own boards when they desire, so you will need to implement a way for certain input words to display a string representation of both boards.

The rest of the style and feel of the game is up to you!