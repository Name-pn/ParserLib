from parser_lib.Analyzer import Analyzer
from parser_lib.LALR.LALRTable import LALRTable
from parser_lib.TreeMixins.MixinCST import MixinCST

import os

class LALRAnalyzerCST(MixinCST, Analyzer):
    def __init__(self, gr):
        MixinCST.__init__(self)
        Analyzer.__init__(self, gr)

    def _create_table(self):
        #if os.path.exists(table_name):
        #    table = pd.read_pickle(table_name)
        #else:
        table = LALRTable(self.gr, False)
        return table
        #return LALRTable(self.gr)

    def parse(self, tokens):
        self.parse_stack.clear()
        self.recognize(tokens)
        if len(self.parse_stack) != 1:
            raise Exception("В стеке не 1 нода")
        return self.parse_stack[0]