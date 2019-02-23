from UserInputParser import UserInputParser


class CommandParser:
    def __init__(self):
        self.inputParser = UserInputParser()
        self.keywords = ["n", "e", "s", "w"]

    def findKeyWords(self, string):
        for word in string.split(" "):
            if word in self.keywords:
                print("{0} found as a keyword".format(word))

commparse = CommandParser()

s = commparse.inputParser.getUserCommand("?")

commparse.findKeyWords(s)
