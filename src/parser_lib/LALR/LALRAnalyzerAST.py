import os

import pandas as pd

from parser_lib.Analyzer import Analyzer
from parser_lib.LALR.LALRTable import LALRTable
from parser_lib.TreeMixins.MixinRegexAST import MixinRegexAST
from parser_lib.const import table_dir, gen_filepath
import hashlib
import pickle
from pathlib import Path

class LALRAnalyzerAST(MixinRegexAST, Analyzer):

    def __init__(self, gr):
        MixinRegexAST.__init__(self)
        Analyzer.__init__(self, gr)

    def gen_and_save_table(self, hash):
        table = LALRTable(self.gr, False)
        Path(table_dir).mkdir(parents=True, exist_ok=True)
        with open(gen_filepath(hash), 'wb') as file:
            pickle.dump(table, file)
        return table

    def _create_table(self):
        now_hash = hashlib.md5(self.gr.__str__().encode('utf-8')).hexdigest()
        table_name = gen_filepath(now_hash)
        if os.path.exists(table_name):
            with open(table_name, 'rb') as file:
                table = pickle.load(file)
        else:
            table = self.gen_and_save_table(now_hash)
        return table
        #return LALRTable(self.gr)

    def parse(self, tokens):
        self.parse_stack.clear()
        self.recognize(tokens)
        if len(self.parse_stack) != 1:
            raise Exception("В стеке не 1 нода")
        return self.parse_stack[0]