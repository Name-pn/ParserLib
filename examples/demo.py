from parser_lib import LALRAnalyzerCST, LALRAnalyzerAST
from parser_lib import Grammar
from parser_lib.Symbol.LTerminal import LTerminal
from parser_lib.Symbol.Terminal import Terminal

class RegexLexer():
    def __init__(self, types):
        self.types = types

    def get_token(self, c):
        match (c):
            case '*':
                return Terminal(self.types['ASTERISK'].name)
            case '|':
                return Terminal(self.types['OR'].name)
            case '(':
                return Terminal(self.types['LEFT_BRACKET'].name)
            case ')':
                return Terminal(self.types['RIGHT_BRACKET'].name)
            case c if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                return LTerminal(c, self.types['SYMBOL'].name)
            case _:
                raise ValueError(f"Unknown character: {c}")

    def tokenize(self, string):
        res = []
        for c in string:
            res.append(self.get_token(c))
        return res


gr = Grammar.load("examples/example_grammar.txt")
print(gr)
lexer = RegexLexer(gr.enum)
parser = LALRAnalyzerCST(gr)
parser2 = LALRAnalyzerAST(gr)

string = 'ab(a|b)*'
tokens = lexer.tokenize(string)
print(tokens)
tree = parser.parse(tokens)
tree2 = parser2.parse(tokens)
print('first\n', tree)
print('second\n', tree2)

print("Good")