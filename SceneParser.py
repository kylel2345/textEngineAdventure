import xml.etree.ElementTree as ET

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
            SceneParser.__instance = self

    def updateScene(self, SceneName):

sp = SceneParser.getInstance()
