class Letters:
    def __init__(self):
        self.letters = """jfhkajfhgjkfhgjhfaghgjkhakhfkjhgfxyz"""
        self.i = 0

    def __next__(self):
        try:
            val = self.letters[self.i]
            self.i += 1
            return val
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


for letter in Letters():
    print(letter)
