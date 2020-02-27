class Item:
    def __init__(self, item_data):
        self.item_name = item_data["Name"]
        self.consumed_on_use    = bool(item_data["ConsumedOnUse"])
        self.usable           = bool(item_data["Usable"])
        self.key_item          = bool(item_data["KeyItem"])
        self.portable         = bool(item_data["Portable"])
        self.weight           = float(item_data["Weight"])
        self.description      = item_data["Description"]

    def __str__(self):
        return self.description

    @property
    def item_name(self):
        return self.__itemName

    @item_name.setter
    def item_name(self, val):
        self.__itemName = val

    @property
    def consumed_on_use(self):
        return self.__consumedOnUse

    @consumed_on_use.setter
    def consumed_on_use(self, val):
        self.__consumedOnUse = val

    @property
    def usable(self):
        return self.__usable

    @usable.setter
    def usable(self, val):
        self.__usable = val

    @property
    def key_item(self):
        return self.__keyItem

    @key_item.setter
    def key_item(self, val):
        self.__keyItem = val

    @property
    def portable(self):
        return self.__portable

    @portable.setter
    def portable(self, val):
        self.__portable = val

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, val):
        self.__weight = val

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, val):
        self.__description = val

    def use(self):
        consumed = False
        if self.usable:
            # TODO: execute an effect, probably need to add an effect to the item xml
            if self.consumed_on_use:
                consumed = True
        else:
            print("{0} is not usable!".format(self.item_name))

        return consumed
