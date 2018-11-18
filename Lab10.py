import random 

guesses = 6

wordTuple = ("awkward", "banjo", "crypt", "dwarf", "fever", "fjord", "gaze", "gypsy", "haiku", "hyper", "ivory",\
"jazzy", "jiffy", "jinx", "kayak", "kiosk", "klutz", "memes", "misty", "naive", "nerdy", "oxen", "pixel", "pick",\
"quip", "quit", "ripen", "rites", "sphere", "speak", "total", "taper", "tuft", "upper", "usual", "wild", "wield",\
"weird", "yacht", "yummy", "zigzag", "zesty", "zion")

def main():
    printInstructions()
    initializeGame()     
     
def printInstructions():
  showInformation("Welcome to Hangman!\n\
Try to guess which letters are in the secret word. \
You have six guesses.")

def initializeGame():
  secretWord = pickAWord(wordTuple)
  copy = secretWord
  gameBoard = getGameBoard(len(secretWord))
  while guesses > 0 and copy != gameBoard:
    print "You have ", guesses, " guesses remaining."
    print "Guess the word:"
    print
    print
    printGameBoard(gameBoard) 
    checkLetter(secretWord, gameBoard)
  if guesses <= 0:
    print "Out of guesses! You lose!"
  elif copy == gameBoard:
    printGameBoard(gameBoard) 
    print "You win!"
  print "Play again!"

   
# Given a tuple of words, pick one at random
# Return an ordered list of the letters that
# make up the word.
def pickAWord(tuple):
  number = random.randint(0, len(tuple) - 1)
  word = tuple[number].lower()
  letterList = []
  for index in range(0, len(word)):
    letterList.append(word[index])
  return letterList
  
def getGameBoard(length):
  gameBoard = []
  for x in range(0, length):
    gameBoard.append("__")
  return gameBoard
       
  
def printGameBoard(gameBoard):
  for element in gameBoard:
    print element ,
  print
  print
    
    
def checkLetter(word, gameBoard):
  guess = requestString('Enter a letter').lower()
  # replace every letter in word that matches the guess
  if guess not in word:
    global guesses
    guesses = guesses - 1
  for index, letter in enumerate(word):
    if letter == guess:
      gameBoard[index] = word[index]
  return gameBoard
      
      
      
  
  
def warmUp():
  name = requestString('What is your name?')
  print name
  message = ''
  while message.lower() != 'stop':
    message = requestString('Input: ')


