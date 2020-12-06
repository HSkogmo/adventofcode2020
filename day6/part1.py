
def read_declaration_forms(file_path):
    groups = []
    with open(file_path, 'r') as file:
        new_group = Group()
        # file.read().splitlines() removes "\n" from the end of the lines
        for line in file.read().splitlines():
            # if the line is empty then we start reading a new groups answers
            if not line.strip():
                print(f'Adding group with answers {new_group.answers}')
                groups.append(new_group)
                new_group = Group()
                continue

            # add each char as an answer to the set
            # sets cannot contain duplicates, so they'll be discarded
            for char in line:
                new_group.answers.add(char)

        # append the last group
        groups.append(new_group)
    return groups


# Is a class really necessary? No, not really. But I kinda like it :)
class Group:
    def __init__(self):
        self.answers = set()


groups = read_declaration_forms('input.txt')

yes_answer_count = 0
for group in groups:
    print(f'Group answered: {group.answers}, total {len(group.answers)} answers')
    yes_answer_count += len(group.answers)

print(f'Sum of Yes answers: {yes_answer_count}')
