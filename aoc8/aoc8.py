grid = [line.strip() for line in open("input.txt")]

len_x, len_y = len(grid[0]), len(grid)
is_in_bounds = lambda pos: 0 <= pos.real < len_x and 0 <= pos.imag < len_x

def find_all_char_positions(char):
    char_positions = set()
    for y_pos, line in enumerate(grid):
        x_pos=-1
        while(x_pos:=line.find(char, x_pos+1)) != -1:
            char_positions.add(x_pos + y_pos * 1j)
    return char_positions

# Get each char type in the grid
from itertools import chain
all_chars = set(chain(*grid))
all_chars.remove(".")

# Find mirror pos
def find_anode(pos1, pos2):
    pos_offset = pos2-pos1
    return pos1-pos_offset

#Part 2 find equally spaced anodes in both directions including original points
anodes = set()
def find_anodes(pos1, pos2):
    # Find anode recursively until out of bounds in both directions
    # Dir 1
    anodes.add(pos1)
    anodes.add(pos2)

    if is_in_bounds(dir_1_anode := find_anode(pos1, pos2)):
        anodes.add(dir_1_anode)
        find_anode(dir_1_anode, pos1)
    
    # Dir 2
    if is_in_bounds(dir_2_anode := find_anode(pos2, pos1)):
        anodes.add(dir_2_anode)
        find_anode(dir_2_anode, pos2)
    


from itertools import permutations
anode_positions = set()
for char in all_chars:
    char_positions = find_all_char_positions(char)
    for pair in permutations(char_positions, 2):
        find_anodes(*pair)

        if is_in_bounds(antinode := find_anode(*pair)):
            anode_positions.add(antinode)

print(len(anode_positions))
print(len(anodes))