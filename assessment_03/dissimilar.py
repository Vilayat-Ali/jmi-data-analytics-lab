def dissim_matrix_nominal(arr: list[str]) -> list[list[int]]:
    dissim_matrix: list[list[int]] = []

    for i in range(len(arr)):
        row = []
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                row.append(0)
            else:
                row.append(1)
        dissim_matrix.append(row)

    return dissim_matrix

def dissim_matrix_ordinal(arr: list[str], order_map: dict[str, int]) -> list[list[int]]:
    dissim_matrix = []
    processed_arr = []

    for value in arr:
        processed_arr.append(order_map[value])

    processed_arr.sort()

    for i in range(len(processed_arr)):
        row = []
        for j in range(len(processed_arr)):
            row.append(abs(processed_arr[i] - processed_arr[j]))

        dissim_matrix.append(row)

    return dissim_matrix

def dissim_matrix_numeric(arr: list[int]) -> list[int]:
    dissim_matrix = []

    max_val = max(arr)
    min_val = min(arr)

    for i in range(len(arr)):
        row = []
        for j in range(len(arr)):
            row.append(abs(arr[i] - arr[j]) / abs(max_val - min_val))
        dissim_matrix.append(row)

    return dissim_matrix