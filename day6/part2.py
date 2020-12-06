
def read_declaration_forms(file_path):
    groups = []
    with open(file_path, 'r') as file:
        new_group = Group()
        # each line contains the answers from a single individual
        # file.read().splitlines() removes "\n" from the end of the lines
        for line in file.read().splitlines():
            person_answers = set()
            # if the line is empty then we start reading a new groups answers
            if not line.strip():
                print(f'Adding group with answers ... {new_group.people_answers}')
                groups.append(new_group)
                new_group = Group()
                continue

            # add each char as an answer to the set for the person
            # sets cannot contain duplicates, so they'll be discarded
            for char in line:
                person_answers.add(char)

            new_group.people_answers.append(person_answers)

        groups.append(new_group)

    return groups


# Is a class really necessary? No, not really. But I kinda like it :)
class Group:
    def __init__(self, people_answers=None):
        if people_answers is None:
            people_answers = list()
        self.people_answers = people_answers

    def get_unanimous_yes_answers(self):
        # take the first set as starting point
        unanimous = self.people_answers[0]
        # find the intersection of all following sets
        for answers in self.people_answers[1:]:
            unanimous = unanimous.intersection(answers)
        return unanimous


groups = read_declaration_forms('input.txt')

unanimous_yes_answer_count = 0
for group in groups:
    print(f'Group answers per individual: {group.people_answers}, unanimous yes: {group.get_unanimous_yes_answers()}')
    unanimous_yes_answer_count += len(group.get_unanimous_yes_answers())

print(f'Unanimous yes count is {unanimous_yes_answer_count}')