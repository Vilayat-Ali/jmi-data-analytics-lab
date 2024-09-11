from assessment_01.util.word_to_vec import Word2Vec

def calc_cosine_similarity(tf_map: dict[str, list[int]]):
    d1_d2_dot = 0
    d1_sq_sum = 0
    d2_sq_sum = 0

    for key in tf_map.keys():
        row = tf_map[key]
        d1_d2_dot += row[0] * row[1]
        d1_sq_sum += row[0] ** 2
        d2_sq_sum += row[1] ** 2

    return d1_d2_dot / (pow(d1_sq_sum, 0.5) * pow(d2_sq_sum, 0.5))


def run_question_02():
    doc_1 = Word2Vec("the_great_expectations.txt")
    doc_2 = Word2Vec("the_treasure_island.txt")

    tf_map: dict[str, list[int]] = {}

    for key in doc_1.frequency_table.keys():
        if key in doc_2.frequency_table:
            tf_map[key] = [doc_1.frequency_table[key], doc_2.frequency_table[key]]

    print(tf_map)

    cos_sim = calc_cosine_similarity(tf_map)

    print(f"Cosine similarity: {cos_sim}")
    print(f"Cosine distance: {1 - cos_sim}")
