from enum import Enum, auto
from typing import Optional

from parser_lib.Symbol.Symbol import Symbol
from parser_lib.Symbol.SymbolType import SymbolType
from dataclasses import dataclass

class Terminal(Symbol):
    def __init__(self, terminal_type: str):
        super().__init__(terminal_type.lower(), SymbolType.TERMINAL)
        self.ttype = terminal_type

    def __str__(self):
        return str(self.value)