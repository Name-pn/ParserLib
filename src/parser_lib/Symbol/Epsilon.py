from parser_lib.Symbol.Symbol import Symbol
from parser_lib.Symbol.SymbolType import SymbolType

class Epsilon(Symbol):
    def __init__(self):
        super().__init__("ε", SymbolType.EPSILON)

EPSILON = Epsilon()