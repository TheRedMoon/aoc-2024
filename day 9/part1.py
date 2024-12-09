
def find_position_first_empty_space(string):
    for i in range(0, len(string)):
        if string[i] == ".":
            return i
    return -1

def create_new_string(string, new_dot_position, new_number_position):
    res_string = string
    value = string[new_dot_position]
    res_string = res_string[:new_number_position] + value + res_string[new_number_position + 1:]
    res_string = res_string[:new_dot_position] + "." + res_string[new_dot_position + 1:]
    return res_string


def move_file(string, position):
    empty_position = find_position_first_empty_space(string)
    if empty_position > position:
        return string
    new_file_string = create_new_string(string, position, empty_position)
    return new_file_string



if __name__ == '__main__':
    with open("day 9/input.txt") as file:
        string = file.read()
    
    # odd positions in the string are empty .
    # replace the numbers at even positions with as many dots as the number
    # for even positions in the string, we replace the number with the number itself times the number
    new_string = ""
    number = 0
    for i in range(0, len(string)):
        if i % 2 == 0:
            new_string = new_string + str(number) * int(string[i])
            number += 1
        else:
            new_string = new_string + "." * int(string[i])
    
    # move end number to first empty space
    print(new_string)
    res_string = new_string
    for i in range(len(new_string) - 1,-1, -1):
        if new_string[i] != ".":
            res_string = move_file(res_string, i)
            

    print(res_string)

    # multiply position index with the value at that index and sum all the values
    sum = 0
    # strip . 
    res_string = res_string.replace(".", "")
    for i in range(0, len(res_string)):
        sum += i * int(res_string[i])
    print(sum)