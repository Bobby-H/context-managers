# Checkpoint #1
class PoemFiles:
  def __init__(self):
    # Checkpoint #2
    print('Creating Poems!')
  # Checkpoint #3
  def __enter__(self):
    print('Opening poem file')
  # Checkpoint #4
  def __exit__(self, *exc):
      print('Closing poem file')
# Checkpoint #5
with PoemFiles() as manager:
  print('Hope is the thing with feathers.')