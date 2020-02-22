import xml.etree.ElementTree as ET
import sys

from ItemParser import ItemParser

from Item import Item
from Char import Char
from Exit import Exit


class SceneParser:

    __instance = None

    xmlTags = ["Desc",
               "Items",
               "Chars",
               "Exits"]

    @staticmethod
    def getInstance():
        if SceneParser.__instance is not None:
            return SceneParser.__instance
        else:
            SceneParser.__instance = SceneParser()
            return SceneParser.__instance

    def __init__(self):
        if SceneParser.__instance is not None:
            raise Exception("attempted another init of a Singleton!")
        else:
            self.__elementTree      = None
            self.__itemParser       = ItemParser.getInstance()
            self.__sDesc            = None
            self.__sItems           = None
            self.__sChars           = None
            self.__sExits           = None
            SceneParser.__instance  = self

    def updateScene(self, SceneName):
        try:
            self.__elementTree = ET.parse("Scenes/{0}.xml".format(SceneName))

        except Exception as e:
            print(e, file=sys.stderr)
            return False

    def parseScene(self):
        try:
            root = self.__elementTree.getroot()
            for tag in SceneParser.xmlTags:
                element = root.find(".//{0}".format(tag))
                if element is not None:
                    self.parseSceneElement(element)
                else:
                    print("could not find tag: {0}".format(tag), file=sys.stderr)

        except Exception as e:
            print(e, file=sys.stderr)

    def parseSceneElement(self, element):
        try:
            # retrieve the attribute for the parsing function we want to use, then call it
            methodName = "parse{0}Tag".format(element.tag)
            method = getattr(self, methodName)
            method(element)

        except Exception as e:
            print("Scene element parsing failed! {0}".format(e), file=sys.stderr)

    def parseDescTag(self, element):
        self.__sDesc = element.text.strip()

    def parseItemsTag(self, element):
        itemNames = SceneParser.parseTagIntoArray(element)
        self.__sItems = []
        for val in itemNames:
            self.__itemParser.updateFile(val)
            newItem = self.__itemParser.returnParsedInfo()
            self.__sItems.append(newItem)

    def parseCharsTag(self, element):
        charNames = SceneParser.parseTagIntoArray(element)
        self.__sChars = []
        for char in charNames:
            self.__sChars.append(Char(char))

    def parseExitsTag(self, element):
        exitNames = SceneParser.parseTagIntoArray(element)
        self.__sExits = []
        for exit in exitNames:
            self.__sExits.append(Exit(exit))

    @staticmethod
    def parseTagIntoArray(tag):
        temp = []
        subTags = tag.findall("Item")
        for value in subTags:  # remove superfluous whitespace, then split on remaining newlines
            temp.append(value.text.strip())  # remove any risidual tabbing of items

        return temp


sp = SceneParser.getInstance()
sp.updateScene("lobbyScene")
sp.parseScene()
