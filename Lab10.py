import random 

guesses = 6
guessedLetters = []
wordTuple = ("awkward", "banjo", "crypt", "dwarf", "fever", "fjord", "gaze", "gypsy", "haiku", "hyper", "ivory",\
"jazzy", "jiffy", "jinx", "kayak", "kiosk", "klutz", "memes", "misty", "naive", "nerdy", "oxen", "pixel", "pick",\
"quip", "quit", "ripen", "rites", "sphere", "speak", "total", "taper", "tuft", "upper", "usual", "wild", "wield",\
"weird", "yacht", "yummy", "zigzag", "zesty", "zion")

def main():
    printInstructions()
    initializeGame()     

# Print the instructions in a pop-up window     
def printInstructions():
  showInformation("Welcome to Hangman!\n\
Try to guess which letters are in the secret word. \
You have six guesses.")

# Initialize and play the game until word is guessed or out of guesses
def initializeGame():
  global guessedLetters
  secretWord = pickAWord(wordTuple)         # An ordered list of letters in word
  gameBoard = getGameBoard(len(secretWord)) # Initally a list of spaces
  while guesses > 0 and secretWord != gameBoard:
    print "You have ", guesses, " guesses remaining."
    print "Guess the word:"
    print
    print
    printGameBoard(gameBoard) 
    checkLetter(secretWord, gameBoard)
    printGuessedLetters(guessedLetters)
  if guesses <= 0:                  # Lose condition
    print "Out of guesses! You lose!"
  elif secretWord == gameBoard:           # Win condition
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

# Makes a list of empty spaces
# Length of this list is as long as the secret word
def getGameBoard(length):
  gameBoard = []
  for x in range(0, length):
    gameBoard.append("__")
  return gameBoard
       
# Prints out the current state of the game
# Includes guessed letters and blanks where letters
# are still unguessed 
def printGameBoard(gameBoard):
  for element in gameBoard:
    print element ,
  print
  print

def printGuessedLetters(guessedLetters):
  print "GUESSED LETTERS: ",
  if len(guessedLetters) > 1:
    for index in range(0, len(guessedLetters) - 1):
      print guessedLetters[index] , 
  print guessedLetters[-1]
    
# Enumerates the ordered list of letters in the word 
# for each position that matches the guessed letter,
# replace the blank on the gameboard at that location
# with the guessed letter
def checkLetter(word, gameBoard):
  global guessedLetters
  guess = requestString('Enter a letter').lower()
  while len(guess) != 1 or not(guess.isalpha()):
    guess = requestString('Invalid guess. Must be a single letter.')
 
  if guess in guessedLetters:
    print "You guessed that letter already!" 
  elif guess not in word:
    global guesses
    guesses = guesses - 1
    guessedLetters.append(guess)
  else:
    guessedLetters.append(guess)
    
  # replace every letter in word that matches the guess  
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


