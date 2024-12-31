starting_digits = [int(num) for num in open("input.txt", "r").readline().strip().split()]
def split_num_into_two(x):
    digit_str = str(x)
    middle_index = int(len(digit_str)/2)
    first_digit = int(digit_str[:middle_index])
    second_digit = int(digit_str[middle_index:])
    return [first_digit, second_digit]


equals_zero = lambda x: x == 0    
has_even_number_of_digits = lambda x: len(str(x))%2 == 0

# advance the starting digits
for iteration in range(25):
    next_digits_set = []
    for digit in starting_digits:
        if equals_zero(digit):
            next_digits_set.append(1)
        elif has_even_number_of_digits(digit):
            next_digits_set.extend(split_num_into_two(digit))
        else:
            next_digits_set.append(digit*2024)
    starting_digits = next_digits_set
print(len(starting_digits))