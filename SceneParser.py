import xml.etree.ElementTree as ET
import sys

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
            #retrieve the attribute for the parsing function we want to use, then call it
            methodName = "parse{0}Tag".format(element.tag)
            method = getattr(self, methodName)
            method(element)

        except Exception as e:
            print("Scene element parsing failed! {0}".format(e), file=sys.stderr)

    def parseDescTag(self, element):
        self.sDesc = element.text.strip()

    def parseItemsTag(self, element):
        self.sItems = SceneParser.parseTagIntoArray(element.text)

    def parseCharsTag(self, element):
        self.sChars = SceneParser.parseTagIntoArray(element.text)

    def parseExitsTag(self, element):
        self.sExits = SceneParser.parseTagIntoArray(element.text)

    @staticmethod
    def parseTagIntoArray(text):
        temp = []
        strippedText = text.strip().split("\n")
        for value in strippedText:  # remove superfluous whitespace, then split on remaining newlines
            temp.append(value.strip()) #remove any risidual tabbing of items

        return temp


sp = SceneParser.getInstance()
sp.updateScene("lobbyScene")
sp.parseScene()
