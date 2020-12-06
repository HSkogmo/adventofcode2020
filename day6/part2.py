
def read_declaration_forms(file_path):
    groups = []
    with open(file_path, 'r') as file:
        # each person answers in the group is added as a set to a list
        people_answers = []
        # file.read().splitlines() removes "\n" from the end of the lines
        for line in file.read().splitlines():
            person_answers = set()
            # if the line is empty then we start reading a new groups answers
            if not line.strip():
                # look through people_answers, extract the common ones from all the answer sets
                # todo: that ^^

                print(f'people answers: {people_answers}')
                common_answers = set()
                print(f'Adding group with answers ...')
                groups.append(Group(common_answers))
                people_answers = []
                continue

            # add each char as an answer to the set
            # sets cannot contain duplicates, so they'll be discarded
            for char in line:
                person_answers.add(char)

            people_answers.append(person_answers)

        print(f'{person_answers}')
        common_answers = set()
        common_answers = person_answers
        groups.append(Group(common_answers))

    return groups


# Is a class really necessary? No, not really. But I kinda like it :)
class Group:
    def __init__(self, answers=None):
        if answers is None:
            answers = set()
        self.answers = answers


groups = read_declaration_forms('input-test.txt')

yes_answer_count = 0
for group in groups:
    print(f'Group answered: {group.answers}, total {len(group.answers)} answers')
    yes_answer_count += len(group.answers)

print(f'Sum of Yes answers: {yes_answer_count}')
