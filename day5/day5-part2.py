import math
import re


def read_boarding_passes(input_file_path):
    boarding_passes = []
    with open(input_file_path, 'r') as file:
        for line in file:
            # each line in the file contains the zone for a boarding pass
            boarding_passes.append(BoardingPass(line))
    return boarding_passes


class BoardingPass:
    PLANE_ROWS = 127
    PLANE_COLUMNS = 7
    def __init__(self, zone):
        self.zone = zone
        self.seat_id = self.get_seat_id()
        print(f'Seat ID: {self.seat_id}')

    def get_seat_id(self):
        row, column = re.findall(r'([B|F]{7})([R|L]{3})', self.zone)[0]
        print(f'Row: {row}, Column: {column}')
        row = self.find(row, 'F', self.PLANE_ROWS)
        column = self.find(column, 'L', self.PLANE_COLUMNS)
        print(f'Row: {row}, Column: {column}')
        return (row * 8) + column

    def find(self, string, keep_left_char, range_max):
        range_foo = (0, range_max)
        for char in string:
            reduced_ranges = self.reduce_range(range_foo)
            range_foo = reduced_ranges[0] if char is keep_left_char else reduced_ranges[1]
            # print(f'{range_foo}')

        return range_foo[0] if string[-1] is keep_left_char else range_foo[1]

    def reduce_range(self, range_limits):
        full_range = list(range(range_limits[0], range_limits[1]+1))
        num_indexes = len(full_range)
        # how can generating a list be avoided? uses a lot of space, but only the 4 values are of interest
        # could they be calculated instead?

        # Identify the two dividing indexes of the full_range when halved
        # Number of indexes is always (observed as) an even number, so should be able to safely divide by 2
        # subtract 1 to account for index 0 and len()
        split_l_idx = int(num_indexes / 2) - 1
        split_r_idx = int(split_l_idx) + 1

        return (range_limits[0], full_range[split_l_idx]), (full_range[split_r_idx], range_limits[1])


boarding_passes = read_boarding_passes('input.txt')
highest_seat_id = 0
lowest_seat_id = math.inf
for bp in boarding_passes:
    highest_seat_id = bp.seat_id if bp.seat_id > highest_seat_id else highest_seat_id
    lowest_seat_id = bp.seat_id if bp.seat_id < lowest_seat_id else lowest_seat_id

# To find the missing IDs in the sequence we can either
# A) generate a list of the range(lo, hi), then iterate through the boarding passes, removing them from the list as they
# are observed. Our missing ID will be left. One pass to find hi/lo values, second pass to eliminate the existing ones.
#
# B) sort the list of boarding_passes according to their seat id and walk the list until we find a break.
# Whatever many passes the sorting algorithm needs (quicksort avg O(nlogn), so worse than O(n)).
# And a second pass to find the break in the sequence.

print(f'Number of boarding passes: {len(boarding_passes)}')
print(f'Highest seat id: {highest_seat_id}')
print(f'Lowest seat id: {lowest_seat_id}')

all_seat_ids = list(range(lowest_seat_id, highest_seat_id+1))

for bp in boarding_passes:
    all_seat_ids.remove(bp.seat_id)

print(f'Remaining seat ids: {all_seat_ids}')