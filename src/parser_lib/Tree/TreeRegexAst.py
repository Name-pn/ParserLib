from enum import Enum, auto

class TypeAst(Enum):
    OR = auto()
    CONCAT = auto()
    KLINI = auto()
    BRACKETS = auto()
    LEAF = auto()

class TreeRegexAstNode():
    def __init__(self, type: TypeAst):
        self.type = type

    def __str__(self, level = 0):
        ret = "-" * level + str(self.__class__.__name__) + "\n"
        if hasattr(self, 'left'):
            ret += self.left.__str__(level+1)
        if hasattr(self, 'right'):
            ret += self.right.__str__(level+1)
        return ret