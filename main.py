import mltk

class Hangman:
  def init():
    self.players = []
    self.state = self.gallows()

  def repr(self):
    self.gallows
    print (f'This is a hangman game, and is a basic hangman game in that sense')

  def play(self):
    self.setup()
    while self.gameover == False:
      guessletter = input(f'Hey there, ' + (self.playername) + ' what is your first guess?') 
      if guessletter not in self.word:
        guessletter = input(f'Sorry' + (self.playername) + '! but thats not right! Next guess?')
        self.structure[9] + (guessletter)
        yield (next.gallows)
      if guessletter in self.word:
        guessletter = input('Congrats ' + (self.playername) + '! ' + (guessletter + ' was in the word, your next guess?')
        for i,guessletter in enumerate(self.wordshow)
          if guessletter == self.word:
              self.wordshow[i] = guessletter

    
  def player(self):
    self.playername = input("Enter your name: ")

  def setup(self):
    with open('words.csv') asf:
      word = list(f)
    gameover = False
    wordshow = []
    for 1 in len(word):
      wordshow + '_'
    self.gallows()
    print wordshow

  def gallows():
    gameover = False
    mistakes = 0
    structure = ['              ______      ',
    '             /     |      ',
    '            /      |      ',
    '           /       ',
    '           |      ',
    '           |       ',
    '           |       ',
    '           |       ',
    '    _______|_________     ']
    print('\n'.join(structure))
    piece1 ='O'
    piece2 ='/'
    piece3 ='|'
    piece4 ='\\'
    piece5 ='|' 
    piece6 =' /'
    piece7 ='/'
    piece8 ='\\'
    piece9 =' \\'
    pieces = [piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9]
    while gameover == False:
       print structure
       structure = (next(structure[3]) + next(pieces[1])
