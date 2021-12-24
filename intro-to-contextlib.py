# Checkpoint #1
from contextlib import contextmanager

# Checkpoint #2
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  # Checkpoint #3
  try:
    yield open_poem_file
  # Checkpoint #4
  finally:
    print('Closing File')
    open_poem_file.close()

# Checkpoint #5
with poem_files('poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.write('Rose is beautiful, Just like you.')
