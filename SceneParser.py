import xml.etree.ElementTree as ET
import sys

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
            self.elementTree    = None
            self.sDesc          = None
            self.sItems         = None
            self.sChars         = None
            self.sExits         = None
            SceneParser.__instance = self

    def updateScene(self, SceneName):
        try:
            self.elementTree = ET.parse("Scenes/{0}.xml".format(SceneName))

        except Exception as e:
            print(e, file=sys.stderr)
            return False

    def parseScene(self):
        try:
            root = self.elementTree.getroot()
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
        self.sDesc = element.text.strip()

    def parseItemsTag(self, element):
        itemNames = SceneParser.parseTagIntoArray(element.text)
        self.sItems = []
        for item in itemNames:
            self.sItems.append(Item(item))

    def parseCharsTag(self, element):
        charNames = SceneParser.parseTagIntoArray(element.text)
        self.sChars = []
        for char in charNames:
            self.sChars.append(Char(char))

    def parseExitsTag(self, element):
        exitNames = SceneParser.parseTagIntoArray(element.text)
        self.sExits = []
        for exit in exitNames:
            self.sExits.append(Exit(exit))

    @staticmethod
    def parseTagIntoArray(text):
        temp = []
        strippedText = text.strip().split("\n")
        for value in strippedText:  # remove superfluous whitespace, then split on remaining newlines
            temp.append(value.strip())  # remove any risidual tabbing of items

        return temp


sp = SceneParser.getInstance()
sp.updateScene("lobbyScene")
sp.parseScene()
