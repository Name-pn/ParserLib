from parser_lib.Symbol.Symbol import Symbol
from parser_lib.Symbol.SymbolType import SymbolType

class NonTerminal(Symbol):
    def __init__(self, value):
        super().__init__(value, SymbolType.NONTERMINAL)

    def __str__(self):
        return str(self.value)