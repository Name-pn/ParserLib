import re
from enum import Enum

from parser_lib.Grammar.ProductionBody import ProductionBody
from parser_lib.Symbol.Epsilon import Epsilon
from parser_lib.Symbol.NonTerminal import NonTerminal
from parser_lib.Grammar.Production import Production
from parser_lib.Symbol.SymbolType import SymbolType#SymbolType
from parser_lib.Symbol.Terminal import Terminal


class Grammar():
    def __init__(self, lst: list[Production], start: NonTerminal = NonTerminal("S"), enum = None):
        self.start = start
        self.dict = lst
        self.enum = enum

    def __str__(self):
        i = 0
        res = ""
        for el in self.dict:
            res += str(i) + " " + str(el) + "\n"
            i += 1
        return res

    def __len__(self):
        return self.dict.__len__()

    def __getitem__(self, item):
        return self.dict[item]

    def save(self, filename: str)->None:
        file = open(filename, 'w', encoding="utf-8")
        file.write("GRAMMAR\n")
        file.write("start: " + str(self.start) + "\n")
        for prod in self.dict:
            file.write(str(prod) + "\n")
        file.close()

    @classmethod
    def parse_terminals(cls, filename):
        with open(filename, 'r', encoding="utf-8") as file:
            file_txt = '\n'.join(file.read().split('\n')[2:])
        matches = re.finditer("[a-z][a-zA-Z0-9_]*", file_txt)
        res = {'UNDEF': 0}
        num_var = 1
        for match in matches:
            name = match.group().upper()
            if name not in res:
                res[name] = num_var
                num_var += 1
        enum = Enum('TokenType', res)
        return enum

    @classmethod
    def load(cls, filename: str)->'Grammar':
        enum = cls.parse_terminals(filename)
        with open(filename, 'r', encoding="utf-8") as file:
            start, lst = cls._parse_grammar_file(file.read(), enum)
        return Grammar(lst, start, enum)

    @classmethod
    def _parse_production(cls, string: str, enum)->ProductionBody:
        symbols = re.split(r"[\s]+", string)
        res = []
        for s in symbols:
            if re.match("[A-Z]", s):
                res.append(NonTerminal(s))
            elif re.match("[a-z]", s):
                cat = enum[s.upper()]
                res.append(Terminal(cat.name))
            elif re.match("ε", s):
                res.append(Epsilon())
        return ProductionBody(res)

    @classmethod
    def _parse_grammar_file(cls, string: str, enum)->tuple[NonTerminal, list[Production]]:
        lst = string.split("\n")
        res = re.match(r"GRAMMAR", lst[0])
        if not res:
            raise Exception("Попытка чтения файла с грамматикой без GRAMMAR в начале")
        res = re.search(r"(?<=start:\s)\S*", lst[1])
        if not res:
            raise Exception("Ошибка чтения стартового нетерминала")
        start = NonTerminal(res.group())
        prod_lst = []
        for index in range(2, len(lst)):
            res = re.match("([A-Z][A-Za-z\S]*)(\s*->\s*)(.+)", lst[index])
            if res:
                non_terminal = NonTerminal(res.group(1))
                body = cls._parse_production(res.group(3), enum)
                prod = Production(non_terminal, body)
                prod_lst.append(prod)
        return (start, prod_lst)

    def append(self, el):
        self.dict.append(el)

    def get_symbols(self):
        st = set()
        for el in self.dict:
            if not el.head in st:
                st.add(el.head)
            for s in el.body.arr:
                if not s in st:
                    st.add(s)
        if Epsilon() in st:
            st.remove(Epsilon())
        return st

    def get_terminals(self):
        s = self.get_symbols()
        res = []
        for el in s:
            if el.type == SymbolType.TERMINAL:
                res.append(el)
        return res

    def get_nonterminals(self)->list[NonTerminal]:
        s = self.get_symbols()
        res = []
        for el in s:
            if el.type == SymbolType.NONTERMINAL:
                res.append(el)
        return res