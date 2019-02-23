
class UserInputParser:
    def __init__(self):
        pass

    def readUserInput(self, prompt):
        return input(prompt)

    def getUserInputInteger(self, prompt):
        try:
            return int(self.readUserInput(prompt))

        except Exception as e:
            print("Sorry, I didn't recognize that, I was expecting an integer")
            return None

    def getUserCommand(self, prompt):
        try:
            return self.readUserInput(prompt)

        except Exception as e:
            print("ERR: could not parse user input.")
            return None
