class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n ')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

# Checkpoint #1
  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    # Checkpoint #2
    self.opened_poem_file.close()

# First
# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ----")
#   print(file.uppercasewords())

# Second
with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print("---- Exception data below ----")

