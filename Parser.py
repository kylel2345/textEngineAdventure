from abc import ABC, abstractmethod

class Parser(ABC):

    xmlTags = None

    def __init__(self):
        super(Parser, self).__init__()

    @staticmethod
    @abstractmethod
    def getInstanc(self):
        pass

    @staticmethod
    @abstractmethod
    def getInstanceWithFilename(self):
        pass

    @abstractmethod
    def updateFile(self):
        pass

    @abstractmethod
    def parseFile(self):
        pass

    @abstractmethod
    def parseElement(self):
        pass
