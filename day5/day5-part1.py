import re
from math import ceil, floor


def read_boarding_passes(input_file_path):
    boarding_passes = []
    with open(input_file_path, 'r') as file:
        for line in file:
            # each line in the file contains the zone for a boarding pass
            boarding_passes.append(BoardingPass(line))
    return boarding_passes


class BoardingPass:
    PLANE_ROWS = 128
    PLANE_COLUMNS = 7
    def __init__(self, zone):
        self.zone = zone
        self.seat_id = self.get_seat_id()

    def get_seat_id(self):
        row, column = re.findall(r'([B|F]{7})([R|L]{3})', self.zone)[0]
        print(f'Row: {row}, Column: {column}')
        row = self.find_row(row)
        column = self.find_column(column)
        print(f'Row: {row}, Column: {column}')

        return (row * 8) + column

    def find_row(self, row_string):
        range = (0, self.PLANE_ROWS)
        for char in row_string:
            # keep the left part of the range if the char is F, else keep the right part
            range = self.reduce_range(range, char == 'F')

        # return either element of the range depending on the final character
        return range[0] if row_string[-1] == "F" else range[1]

    def find_column(self, column_string):
        range = (0, self.PLANE_COLUMNS)
        for char in column_string:
            print(f'{range}')
            range = self.reduce_range(range, char == 'L')

        return range[0] if column_string[-1] == 'L' else range[1]

    def reduce_range(self, range, keep_left):
        diff = (range[1] - range[0]) / 2
        # print(f'{range}, {diff}')
        if keep_left:
            # diff = floor(diff)
            return range[0], (range[0] + diff)
        else:
            # diff = ceil(diff)
            return (range[1] - diff), range[1]


# boarding_passes = read_boarding_passes('input.txt')
# for bp in boarding_passes:
#     bp.get_seat()

# boarding_passes = read_boarding_passes('input-test.txt')
# for bp in boarding_passes:
#     print(bp.seat_id)

bp = BoardingPass('BBFFBBFRLL')
print(bp.seat_id)