import xml.etree.ElementTree as ET
import sys

class SceneParser:

    __instance = None

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
            self.elementTree =  None
            self.sDesc =        None
            self.sItems =       None
            self.sChars =       None
            self.sExits =       None
            SceneParser.__instance = self

    def updateScene(self, SceneName):
        try:
            self.elementTree = ET.parse("Scenes/{0}.xml".format(SceneName))

        except Exception as e:
            print(e, file=sys.stderr)
            return False

    def parseScene(self):
        root = self.elementTree.getRoot
        for child in root: #note this assumes that the xml fields are in the correct order
            print(child.name)


sp = SceneParser.getInstance()
sp.updateScene("exampleScene")
sp.parseScene()
