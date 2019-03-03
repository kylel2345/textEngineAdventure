class Item:
    def __init__(self, itemName):
        self.itemName = itemName

        self.xmlTags = [
            "name",
            "desc",
            "pickup",
            "drop"
        ]
