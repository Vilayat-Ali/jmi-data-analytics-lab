import logging
from .data import data
from .dissimilar import dissim_matrix_nominal, dissim_matrix_ordinal, dissim_matrix_numeric
from .utils import pretty_print_matrix

def main():
    logging.info(f"PREPROCESSING NOMINAL FIELD `Test-1`")
    nominal_fields = data['test_01']
    ordinal_fields = data['test_02']
    numeric_fields = data['test_03']

    # dissimilarity matrix of nominal values
    d_nominal = dissim_matrix_nominal(nominal_fields)
    pretty_print_matrix("D-Matrix for Nominal Values", d_nominal)

    # dissimilarity matrix of ordinal 
    order: dict[str, int] = {
        'Low Priority': 0,
        'High Priority': 1,
        'Urgent': 2
    }
    d_ordinal = dissim_matrix_ordinal(ordinal_fields, order)
    pretty_print_matrix("D-Matrix for Ordinal Values", d_ordinal)

    # dissimilarity matrix of numeric values
    d_numeric = dissim_matrix_numeric(numeric_fields)
    pretty_print_matrix("D-Matrix for Numerical Values", d_numeric)

    logging.info(f"Dataset after preprocessing of nominal values {data}")
    print(data)
    print()

    logging.info(f"Combining the values to find distance matrix")

    comb_matrix: list[list[int]] = []

    for row_idx in range(len(d_numeric)):
        com_mat_row: list[str] = []

        for cell_idx in range(len(d_nominal[0])):
            ord_val = d_ordinal[row_idx][cell_idx]
            nom_val = d_nominal[row_idx][cell_idx]
            num_val = d_numeric[row_idx][cell_idx]
            com_mat_row.append((ord_val + nom_val + num_val) / 3)
        
        comb_matrix.append(com_mat_row)

    pretty_print_matrix("D-Matrix of combined values", comb_matrix)

if __name__ == '__main__':
    main()