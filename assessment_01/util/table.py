class Table:
    def __init__(self, headers: list[str], rows: list[list[any]]):
        if len(headers) != len(rows[0]):
            raise "Header count doesnt match column size of rows provided!"

        self.headers = headers
        self.rows = []
        self.col_widths: list[int] = []

        for header in self.headers:
            self.col_widths.append(len(header) + 2)

        for row in rows:
            str_row = []
            for col_idx in range(len(row)):
                col_str = str(row[col_idx])
                str_row.append(col_str)
                self.col_widths[col_idx] = max(len(str_row) + 2, self.col_widths[col_idx])
            self.rows.append(str_row)

    def print(self, limit: None | int = None):
        self.__print_hr_line()
        self.__print_table_row(self.headers)
        self.__print_hr_line()
        if limit is None:
            for row in self.rows:
                self.__print_table_row(row)
        else:
            if(limit > 0 and limit > len(self.rows)):
                Exception()
            lim_count = limit
            idx = 0
            while lim_count > 0:
                self.__print_table_row(self.rows[idx])
                idx += 1
                lim_count -= 1
        self.__print_hr_line()

    def __print_table_row(self, row: list[str]):
        table_row = "|"
        for idx in range(len(self.col_widths)):
            table_row += " "
            space_count = self.col_widths[idx] - len(row[idx]) - 2
            for _ in range(space_count):
                table_row += " "
            table_row += row[idx]
            table_row += " |"
        print(table_row)

    def __print_hr_line(self):
        hr_line = "+"
        for col_width in self.col_widths:
            for _ in range(col_width):
                hr_line += "-"
            hr_line += "+"
        print(hr_line)
