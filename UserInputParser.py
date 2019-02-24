
class UserInputParser:
    """Singleton"""

    __instance = None

    def __init__(self):
        if UserInputParser.__instance is not None:
            raise Exception("attempted another init of a Singleton!")
        else:
            UserInputParser.__instance = self

    @staticmethod
    def getInstance():
        if UserInputParser.__instance is not None:
            return UserInputParser.__instance
        else:
            UserInputParser.__instance = UserInputParser()
            return UserInputParser.__instance

    @staticmethod
    def getUserInput(prompt):
        return input(prompt)

    @staticmethod
    def getUserInputInteger(prompt):
        try:
            return int(UserInputParser.getUserInput(prompt))

        except Exception as e:
            print("Sorry, I didn't recognize that, I was expecting an integer")
            return None

    @staticmethod
    def getUserCommand(prompt):
        try:
            return UserInputParser.getUserInput(prompt)

        except Exception as e:
            print("ERR: could not parse user input.")
            return None
