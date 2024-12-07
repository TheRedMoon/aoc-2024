import operator
import time
operations = {
    '+': operator.add,
    '*': operator.mul,
    "||": operator.concat,
}

if __name__ == '__main__':
    start = time.time()
    operators = ['+', '*', "||"]
    with open("input.txt") as file:
        lines = [line.rstrip('\n') for line in file]
    list_of_valid_answers = []
    for line in lines:
        split = line.split(":")
        ans = split[0].strip()
        equat = split[1].strip()
        equation_nr = equat.split(" ")
        list_of_sub_equatios_results = [int(equation_nr[0])]
        found_result = False
        for x, number in enumerate(equation_nr):
            if found_result:
                break
            #check if x+1 is valid
            if x+1 < len(equation_nr):
                # either + or * 
                # also check if last operation
                last = False
                if x+2 >= len(equation_nr):
                    last = True
                list_of_operator_results = []
                for y, op in enumerate(operators):
                    if found_result:
                        break

                    for sub_res in list_of_sub_equatios_results:
                        if op == "||":
                            concat = operations[op](str(sub_res), str(equation_nr[x+1]))
                            result = int(concat)
                        else:
                            result = operations[op](int(sub_res), int(equation_nr[x+1]))

                        if result == int(ans) and last:
                            list_of_valid_answers.append(int(result))
                            found_result = True
                            break
                        else:
                            if result > int(ans):
                                continue
                            if not last:
                                list_of_operator_results.append(result)
                        ## if last operation                            
                list_of_sub_equatios_results = []
                list_of_sub_equatios_results.extend(list_of_operator_results)
                list_of_operator_results = []
    print(sum(list_of_valid_answers))
    end = time.time()
    print("Time taken:", end - start) # 5 seconds
