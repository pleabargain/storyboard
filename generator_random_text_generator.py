import random
def primary():
  f = open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/adjectives.txt")
  quotes = f.readlines()
  f.close()

  sampling = random.sample(quotes, 1)
  for sample in sampling: print(sample)


if __name__== "__main__":
  primary()