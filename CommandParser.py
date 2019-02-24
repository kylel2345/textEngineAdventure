from UserInputParser import UserInputParser


class CommandParser:

    __instance = None

    @staticmethod
    def getInstance():
        if CommandParser.__instance is not None:
            return CommandParser.__instance
        else:
            CommandParser.__instance = CommandParser()
            return CommandParser.__instance

    def __init__(self):
        if CommandParser.__instance is not None:
            raise Exception("attempted another init of a Singleton!")
        else:
            self.inputParser = UserInputParser.getInstance()
            self.keywords = ["n", "e", "s", "w"]
            CommandParser.__instance = self

    def findKeyWords(self, string):
        for word in string.split(" "):
            if word in self.keywords:
                print("{0} found as a keyword".format(word))

commparse = CommandParser.getInstance()

s = commparse.inputParser.getUserCommand("?")

commparse.findKeyWords(s)
