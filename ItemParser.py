import xml.etree.ElementTree as ET
from Parser import Parser
from Item import Item
import sys


class ItemParser(Parser):
    __instance = None

    xmlTags = ["Name",
               "Description",
               "Weight",
               "KeyItem",
               "Usable",
               "ConsumedOnUse",
               "Portable"]

    @staticmethod
    def getInstance():
        if ItemParser.__instance is None:
            ItemParser.__instance = ItemParser()

        return ItemParser.__instance

    @staticmethod
    def getInstanceWithFilename(filename):
        if ItemParser.__instance is None:
            ItemParser.__instance = ItemParser()

        ItemParser.__instance.updateFile(filename)

        return ItemParser.__instance

    def __init__(self):
        if ItemParser.__instance is not None:
            raise Exception("attempted another init of a Singleton!")
        else:
            self.__elementTree        = None
            self.__itemData         = {}
            self.__filename           = None
            ItemParser.__instance   = self

    def updateFile(self, fileName):
        try:
            self.__filename = fileName
            self.__itemData = {}
            self.__elementTree = ET.parse("Items/{0}.xml".format(fileName))

        except Exception as e:
            print(e, file=sys.stderr)
            return False

    def parseFile(self):
        try:
            root = self.__elementTree.getroot()
            for tag in ItemParser.xmlTags:
                element = root.find(".//{0}".format(tag))
                if element is not None:
                    self.parseElement(element)
                else:
                    print("ERR ItemParser({0}) could not find tag: {1}".format(self.__filename, tag), file=sys.stderr)

        except Exception as e:
            print(e, file=sys.stderr)

    def parseElement(self, element):
        self.__itemData[element.tag] = element.text.strip()

    def packageParsedInfo(self):
        dict = {}
        for entry in ItemParser.xmlTags:
            dict[entry] = self.__itemData[entry]

        return dict

    def returnParsedInfo(self):
        self.parseFile()
        data = self.packageParsedInfo()
        return Item(data)

