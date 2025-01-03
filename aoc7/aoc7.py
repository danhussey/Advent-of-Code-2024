# Get the test values and equation operands into a tuple of (int, list[int])
with open("aoc7/input.txt", "r") as file:
    lines = [line.strip().split(" ") for line in file]

# Func that gets all possible equation results and returns true if test result can be reached
from itertools import product
from functools import reduce
def is_possibly_true_equation (test_value: int, operands: list[int]):
    possible_operations_lists = list(product(["*", "+"], repeat=len(operands)-1))
    
    for operations_list in possible_operations_lists:
        vals_ops = zip(operands[1:], operations_list)
        res = reduce(lambda acc, val_op: (acc + val_op[0] if val_op[1]=="+" else acc*val_op[0]),
                     vals_ops,
                     operands[0])

        if res == test_value:
            print("Found " + str(operations_list) + " for " + str(operands) + " == " + str(test_value))
            return True
    return False

# Collects test values with valid equation results
sum = 0
for line in lines:
    test_val = int(line[0].strip(":"))
    operands = list(map(int, line[1:]))
    if is_possibly_true_equation(test_val, operands):
        sum += test_val
print(sum)


# Part 2
def is_possibly_true_equation_pt2 (test_value: int, operands: list[int]):
    possible_operations_lists = product(["*", "+", "||"], repeat=len(operands)-1)
    
    for operations_list in possible_operations_lists:
        res = operands[0]
        for vals_ops in zip(operands[1:], operations_list):
            
        res = reduce(lambda acc, val_op: (acc + val_op[0] if val_op[1]=="+" else acc*val_op[0]),
                     vals_ops,
                     operands[0])

        if res == test_value:
            print("Found " + str(operations_list) + " for " + str(operands) + " == " + str(test_value))
            return True
    return False
