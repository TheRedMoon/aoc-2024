import operator
import itertools

operations = {
    '+': operator.add,
    '*': operator.mul,
}

def evaluate_equation(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        result = operations[operators[i]](result, numbers[i + 1])
    return result

if __name__ == '__main__':
    operators = ['+', '*']
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]

    list_of_valid_answers = []

    for line in lines:
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split(" ")))

        num_operators = len(numbers) - 1
        found_valid = False

        # Generate all possible operator combinations
        for operator_combination in itertools.product(operators, repeat=num_operators):
            result = evaluate_equation(numbers, operator_combination)
            if result == target:
                list_of_valid_answers.append(target)
                found_valid = True
                break  


    print(sum(list_of_valid_answers))
