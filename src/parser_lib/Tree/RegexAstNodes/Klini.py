from parser_lib.Tree.TreeRegexAst import TreeRegexAstNode, TypeAst


class KliniNode(TreeRegexAstNode):
    def __init__(self, left):
        super().__init__(TypeAst.KLINI)
        self.left = left