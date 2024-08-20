from ..util.word_to_vec import Word2Vec
from ..util.table import Table

def run_ques_02():
    doc = Word2Vec("the_great_expectations.txt")
    table_headers = ["Word (Term)", "Term Frequency"]

    table_data: list[list[str, int]] = []

    # printing the table
    for key in doc.frequency_table.keys():
        table_data.append([str(key), doc.frequency_table[key]])

    table = Table(table_headers, table_data)
    
    table.print(20)

    # making vector
    tf_vec = doc.get_term_freq_vector()

    print(tf_vec)