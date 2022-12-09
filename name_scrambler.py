import random


def scramble_list(list):
    new_list = []
    if len(list) <= 1:
        return new_list
    while not no_match(new_list, list):
        new_list = []

        #work on intended cases only
        used = [-1]
        random_number = -1
        for item in list:
            while random_number in used:  #get a new random random_number
                random_number = random.randint(0, len(list)-1)

            #use random_number
            new_list = new_list + [list[random_number]]

            #mark random_number as used
            used = used + [random_number]

    return new_list

def no_match(set_list, randomized_list):
    if len(set_list) != len(randomized_list):
        #print('list sizes are not the same')
        return False

    for i in range(len(set_list)):
        if set_list[i] == randomized_list[i]:
            return False

    return True
