class Item:
    def __init__(self, itemName):
        self.itemName = itemName

        self.__name = None
        self.__consumedOnUse    = None
        self.__interactable     = None
        self.__keyItem          = None
        self.__portable         = None
        self.__Weight           = None
