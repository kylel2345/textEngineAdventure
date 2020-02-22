class Item:

    def __init__(self, itemData):
        self.__itemName = itemData["Name"]
        self.__consumedOnUse    = bool(itemData["ConsumedOnUse"])
        self.__usable           = bool(itemData["Usable"])
        self.__keyItem          = bool(itemData["KeyItem"])
        self.__portable         = bool(itemData["Portable"])
        self.__Weight           = float(itemData["Weight"])
        self.__Description      = itemData["Description"]

