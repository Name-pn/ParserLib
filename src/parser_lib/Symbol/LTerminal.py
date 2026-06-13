from parser_lib.Symbol.Terminal import Terminal


class LTerminal(Terminal):
    def __init__(self, lexem:str, category):
        super().__init__(category)
        self.lexem = lexem

    # def __str__(self):
    #     return str(self.lexem)
    #
    # def __repr__(self):
    #     return str(self.lexem)