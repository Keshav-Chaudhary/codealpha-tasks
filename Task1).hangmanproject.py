import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ["java", "python", "javascript", "css", "scala", "ruby", "pascal", "kotlin", "swift", "sql", "html", "rust", "perl"]
lives = 7
wordchoice = random.choice(words)
#print("word choosed by random module : ",wordchoice)
a = ['_' for k in range(len(wordchoice))]
GameOver = False
while not GameOver:
    userguess = input("Please Guess the character: ")
    for i in range(len(wordchoice)):
        let = wordchoice[i]
        if let == userguess:
            a[i] = userguess
    print(a)
    if userguess not in wordchoice:
        print(HANGMANPICS[7-lives])
        lives -= 1
        print("Remaining Lives",lives)
        if lives == 0:
            GameOver = True
            print("!! GAME OVER !!")
    if "_" not in a:
        GameOver = True
        print("!! You Won !!")
