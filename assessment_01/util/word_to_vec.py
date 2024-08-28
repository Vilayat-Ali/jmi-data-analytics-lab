import os
from ..constants import stop_words

def clean_string(line: str) -> str:
    # remove 's to omit handling apostophied words
    special_chars = [",", ".", "{", "}", "[", "]", "(", ")", ";", ":", "\"", "\n", "!", "\\", "'s"]
    
    # Replace each special character
    for special_char in special_chars:
        line = line.replace(special_char, "")
    
    return line

class Word2Vec:

    def __init__(self, filepath):
        try:
            self.frequency_table: dict[str, int] = {}

            # Reading document at filepath
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.filepath = os.path.join(project_root, 'data', filepath)

            if not os.path.exists(self.filepath):
                raise FileNotFoundError(f"The file {self.filepath} does not exist.")    

            with open(self.filepath, 'r') as document:
                for line in document:
                    words = clean_string(line).split()
                    for word in words:
                        if word not in stop_words:
                            if word not in self.frequency_table:
                                self.frequency_table[word.lower()] = 1
                            else:
                                self.frequency_table[word.lower()] += 1                 

            self.words = sorted([word for word in self.frequency_table.keys()])
        except FileNotFoundError as e:
            print(e)

    def get_term_freq_vector(self) -> list[list[str], list[int]]:
        vec: list[list[str], list[int]] = [[], []]

        for key in self.frequency_table.keys():
            vec[0].append(key)
            vec[1].append(self.frequency_table[key])

        return vec