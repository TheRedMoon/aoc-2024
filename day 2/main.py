def is_valid_number(number, lower, upper):
    return lower <= number <= upper

def is_safe_report(levels):
    increased = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        difference = abs(levels[i] - levels[i + 1])
        if (levels[i] < levels[i + 1]) != increased or not is_valid_number(difference, 1, 3):
            return False
    return True

def is_safe_with_dampener(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe_report(modified_levels):
            return True
    return False

if __name__ == '__main__':
    with open("day 2/input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
        
    safe_pt1 = 0
    safe_pt2 = 0
    #part 1
    for line in lines:
        numbers = [int(x) for x in line.split()]
        if is_safe_report(numbers):
            safe_pt1 += 1

    print("Number of safe reports part 1:", safe_pt1)

    # part 2
    for line in lines:
        numbers = [int(x) for x in line.split()]
        if is_safe_with_dampener(numbers):
            safe_pt2 += 1

    print("Number of safe reports part 2:", safe_pt2)
