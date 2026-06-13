from parser_lib.Tree.TreeRegexAst import TreeRegexAstNode, TypeAst


class LeafNode(TreeRegexAstNode):
    def __init__(self, attr):
        super().__init__(TypeAst.LEAF)
        self.attr = attr