from ..util.word_to_vec import Word2Vec
from ..util.table import Table

def common_term_frequency(doc_1: Word2Vec, doc_2: Word2Vec) -> list[list[str, str]]:
    common_term_ft: dict[str, int] = {}


def run_ques_02():
    doc_1 = Word2Vec("the_great_expectations.txt")
    doc_2 = Word2Vec("the_treasure_island.txt")
    table_headers = ["Common Word (Term)", "Term Frequency"]

    common_term_map: dict[str, int] = {}

    for key in doc_1.frequency_table.keys():
        if key in doc_2.frequency_table:
            common_term_map[key] = min(doc_1.frequency_table[key], doc_2.frequency_table[key])



    # table_data: list[list[str, int]] = []

    # table = Table(table_headers, table_data)
    
    # table.print(20)

    # making vector
    vec = []

    # for key in common_term_map.keys():
    #     vec.append(

    #     )

    print(common_term_map)