table_dir = "./parser_data/"

def gen_filepath(hash_str):
    return table_dir + "table_" + hash_str[:8] + ".pkl"