
# Input reading
grid = [line.strip() for line in open("aoc6/input.txt", "r")]
x_len, y_len = len(grid[0]), len(grid)

def find_guard(grid):
    for curr_y_pos, line in enumerate(grid):
        if (found_x_pos := line.find("^")) != -1:
            return (found_x_pos, curr_y_pos)
    return None

def is_in_bounds(pos):
    x, y = pos
    return 0 <= x < x_len and 0 <= y < y_len

dir_offsets = {"up":(0,-1), "right":(1,0), "down":(0,1), "left":(-1,0)}
dirs =  ["up", "right", "down", "left"]
curr_dir_idx = 0

curr_pos = find_guard(grid)
curr_dir = "up"
traversed = {curr_pos}

while True:
    # Try move guard in guard_dir from guard_pos
    new_pos = tuple([a+b for a,b in zip(curr_pos, dir_offsets[curr_dir])])
    if not(is_in_bounds(new_pos)):
        break
    next_char = grid[new_pos[1]][new_pos[0]]

    if (next_char != "#"):
        # Mark down new pos
        traversed.add(new_pos)
        print("Moved " + str(curr_pos) + " to " + str(new_pos) + f"{curr_dir} ({next_char})")
        curr_pos, curr_dir =  new_pos, curr_dir

    else: 
        # Try other direction
        print(f"Next char not free: {next_char}. Trying new dir.")
        curr_dir_idx = (curr_dir_idx + 1) % 4
        curr_pos, curr_dir =  curr_pos, dirs[curr_dir_idx]

print(len(traversed))