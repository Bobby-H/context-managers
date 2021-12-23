# Checkpoint #1
class PoemFiles:
    def __init__(self, poem_file, mode):
        print('Starting up a poem context manager')
        self.poem_file = poem_file
        self.mode = mode
# Checkpoint #2
    def __enter__(self):
        print('Opening poem file')
        self.opened_poem_file = open(self.file, self.mode)
        return self.opened_poem_file
# Checkpoint #3
    def __exit__(self, *exc):
        print('Closing poem file')
        self.opened_poem_file.close()

# with PoemFiles('poem.txt', 'w') as open_poem_file:
#    open_poem_file.write('Hope is the thing with feathers')