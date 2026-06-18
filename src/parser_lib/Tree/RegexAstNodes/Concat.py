from parser_lib.Tree.TreeRegexAst import TreeRegexAstNode, TypeAst


class ConcatNode(TreeRegexAstNode):
    def __init__(self, left, right):
        super().__init__(TypeAst.CONCAT)
        self.left = left
        self.right = right