# Get the test values and equation operands into a tuple of (int, list[int])
with open("aoc7/input.txt", "r") as file:
    lines = [line.strip().split(" ") for line in file]

# Func that gets all possible equation results 
from itertools import product
def is_possibly_true_equation (test_value: int, operands: list[int]):
    num_pairs = len(operands)-1
    operators = ["*", "+"]
    possible_operations_lists = list(product(operators, repeat=num_pairs))
    # print(possible_operations_lists)
    results = []
    for operations_list in possible_operations_lists:
        result = operands[0]
        for pos, next_operand in enumerate(operands[1:]):
            if operations_list[pos]=="*":
                result = result*next_operand
            elif operations_list[pos]=="+":
                result+=next_operand
            else:
                print("Something's wrong.")

        if result == test_value:
            print("Found " + str(operations_list) + " for " + str(operands) + " == " + str(test_value))
            return True
    return False


print(is_possibly_true_equation(3267, [81, 40, 27]))
# Collects test values with valid equation results
sum = 0
for line in lines:
    test_val = int(line[0].strip(":"))
    operands = list(map(int, line[1:]))
    if is_possibly_true_equation(test_val, operands):
        sum += test_val