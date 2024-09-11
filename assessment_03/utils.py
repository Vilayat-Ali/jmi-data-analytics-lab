def __print_hr_line(length: int):
    hr = "+"
    for _ in range(length):
        hr += '-'

def pretty_print_matrix(matrix_label: str, arr: list[list[any]]):
    print(f"Matrix: {matrix_label}")

    for rows in arr:
        print(rows)

    print("")
