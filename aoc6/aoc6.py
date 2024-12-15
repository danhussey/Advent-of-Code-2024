
def guard_pos(grid):
    for curr_y_pos, line in enumerate(grid):
        if (found_x_pos := line.find("^")) != -1:
            return (found_x_pos, curr_y_pos)
    return (-1,-1) # Not found

grid = [line.strip() for line in open("aoc6/input.txt", "r")]
dirs = {"up":(0,-1), "right":(1,0), "down":(0,1), "left":(-1,0)}
x_len = len(grid[0])
y_len = len(grid)
curr_dir = "up"
curr_pos = guard_pos(grid)
traversed = {curr_pos}

def next_dir (curr_dir):
    match curr_dir:
        case "up":
            return "right"
        case "right":
            return "down"
        case "down":
            return "left"
        case "left":
            return "up"
    return ""

def move_guard(guard_pos, guard_dir):
    # Try move guard in guard_dir from guard_pos
    new_pos = tuple([a+b for a,b in zip(guard_pos, dirs[guard_dir])])
    if not(0 <= new_pos[0] < x_len and 0 <= new_pos[1] < y_len):
        return -1, -1
    next_char = grid[new_pos[1]][new_pos[0]]

    if (next_char != "#"):
        # Mark down new pos
        traversed.add(new_pos)
        print("Moved " + str(guard_pos) + " to " + str(new_pos) + f"{curr_dir} ({next_char})")
        return new_pos, guard_dir

    else: 
        # Try other direction
        print(f"Next char not free: {next_char}. Trying new dir.")
        return guard_pos, next_dir(guard_dir)
    
while ((curr_pos, curr_dir) != (-1, -1)):
    curr_pos, curr_dir = move_guard(curr_pos, curr_dir)

print(len(traversed))