from parser_lib.Tree.TreeRegexAst import TreeRegexAstNode, TypeAst


class OrNode(TreeRegexAstNode):
    def __init__(self, left, right):
        super().__init__(TypeAst.OR)
        self.left = left
        self.right = right