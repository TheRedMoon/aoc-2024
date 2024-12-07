
INFINITY = 1000000

def get_all_substring_starting_with(str, startswith):
    res = []
    for i in range(len(str)):
        if str[i:].startswith(startswith): # strip the string from the start index and check if it starts with the given string
            res.append(str[i:])  # if it does, append it to the result, this means we
    return res

def get_all_substring_starting_with_index(str, startswith):
    res = []
    for i in range(len(str)):
        new_str = str[i:]
        if new_str.startswith(startswith): # strip the string from the start index and check if it starts with the given string
            res.append(i)  # if it does, append it to the result, this means we
    return res

def is_valid_int(str):
    try:
        int(str)
        if len(str) > 3:
            return False
        return True
    except ValueError:
        return False

def get_mults(res):
    mults = []
    for mul in res:
        str = mul[4:]
        # get string till the next comma
        first_comma = str.index(",")
        first_int = str[:first_comma]
        if not is_valid_int(first_int):
            continue
        second_int = str[first_comma+1:str.index(")")]
        if not is_valid_int(second_int):
            continue

        mults.append(int(first_int)*int(second_int))
    return mults

def get_closest_index_nr_distance(ind, list):
    closest_index_nr_distance = INFINITY
    for i in range(len(list)):
        if list[i] < ind and ind - list[i] < closest_index_nr_distance:
            closest_index_nr_distance = ind - list[i]
    return closest_index_nr_distance


def get_mults_through_index(str, mult_ind, dos, donts):
    mults = []
    for ind in mult_ind:
        relevant_str = str[ind+4:]
        dos_index_dist = get_closest_index_nr_distance(ind, dos)
        donts_index_dist = get_closest_index_nr_distance(ind, donts)
        if donts_index_dist < dos_index_dist:
            continue        
        # get string till the next comma
        first_comma = relevant_str.index(",")
        first_int = relevant_str[:first_comma]
        if not is_valid_int(first_int):
            continue
        second_int = relevant_str[first_comma+1:relevant_str.index(")")]
        if not is_valid_int(second_int):
            continue

        mults.append(int(first_int)*int(second_int))
    return mults

if __name__ == '__main__':
    with open("day 3/input.txt") as file:
        str = file.read()

    # part 1
    res = get_all_substring_starting_with(str, "mul(",)
    mult_res = get_mults(res)
    print (sum(mult_res))
    
    # part 2
    mult_ind = get_all_substring_starting_with_index(str, "mul(",)
    dos = get_all_substring_starting_with_index(str, "do()")
    donts = get_all_substring_starting_with_index(str, "don't()")
    mult_res = get_mults_through_index(str, mult_ind, dos, donts)
    print (sum(mult_res))

