from parser_lib.Symbol.Symbol import Symbol
from parser_lib.Symbol.SymbolType import SymbolType

class Dot(Symbol):
    def __init__(self):
        super().__init__("•", SymbolType.DOT)