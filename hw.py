class reverse:
    def __init__(self, s):
        self.s = s

    def __word__(self):

        j = self.s[::-1]
        print(j)


string = reverse(input('Enter string:'))

print(string.__word__())
