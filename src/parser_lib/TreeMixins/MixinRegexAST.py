from parser_lib.Symbol.Epsilon import Epsilon
from parser_lib.Symbol.LTerminal import LTerminal
from parser_lib.Symbol.Symbol import Symbol
from parser_lib.Symbol.Terminal import Terminal
from parser_lib.Tree.RegexAstNodes.Concat import ConcatNode
from parser_lib.Tree.RegexAstNodes.Klini import KliniNode
from parser_lib.Tree.RegexAstNodes.Leaf import LeafNode
from parser_lib.Tree.RegexAstNodes.Name import NameNode
from parser_lib.Tree.RegexAstNodes.Or import OrNode


class MixinRegexAST():
    def __init__(self):
        self.parse_stack = []

    def _on_reduce0(self):
        pass

    def _on_reduce1(self):
        length = 3
        t = self.parse_stack[-1]
        r = self.parse_stack[-3]
        del self.parse_stack[-length:]
        new_node = OrNode(r, t)
        self.parse_stack.append(new_node)

    def _on_reduce2(self):
        pass

    def _on_reduce3(self):
        length = 2
        f = self.parse_stack[-1]
        t = self.parse_stack[-2]
        del self.parse_stack[-length:]
        new_node = ConcatNode(t, f)
        self.parse_stack.append(new_node)

    def _on_reduce4(self):
        pass

    def _on_reduce5(self):
        length = 2
        f = self.parse_stack[-2]
        del self.parse_stack[-length:]
        new_node = KliniNode(f)
        self.parse_stack.append(new_node)

    def _on_reduce6(self):
        pass
    def _on_reduce7(self):
        length = 3
        r = self.parse_stack[-2]
        del self.parse_stack[-length:]
        self.parse_stack.append(r)

    def _on_reduce8(self):
        length = 3
        r = self.parse_stack[-2]
        del self.parse_stack[-length:]
        self.parse_stack.append(r)

    def _on_reduce9(self):
        pass

    def _on_reduce(self, state, symbol, action):
        index = action.value
        method_name = "_on_reduce" + str(index)
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            method()
        else:
            raise Exception(f"Не найдена свертка {index}")

    def _on_shift(self, state, symbol):
        if not isinstance(symbol, Terminal):
            raise Exception("Передан не терминальный символ")
        if isinstance(symbol, LTerminal):
            if len(symbol.lexem) > 1:
                self.parse_stack.append(NameNode(symbol))
            else:
                self.parse_stack.append(LeafNode(symbol))
        else:
            self.parse_stack.append(LeafNode(symbol))


