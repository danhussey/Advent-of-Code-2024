trailmap = [line.strip() for line in open("aoc10/input.txt")]

def is_in_bounds(pos, trailmap):
    return 0 <= pos[0] < len(trailmap[0]) and 0 <= pos[1] < len(trailmap)

# Determine traversability
def is_traversible(origin, dest, trailmap):
    if is_in_bounds(dest, trailmap):
        return int(trailmap[origin[1]][origin[0]]) - int(trailmap[dest[1]][dest[0]]) == -1
    else:
        return False

# Find traversible positions from a point
def find_traversible_neighbours(origin, trailmap):
    offsets = [(0,-1), (1,0), (0,1), (-1, 0)]   # up right down left
    new_positions = map(lambda offset: (origin[0]+offset[0], origin[1]+offset[1]), offsets)
    # Return positions that are in bounds and traversible
    return list(filter(lambda new_pos: is_traversible(origin, new_pos, trailmap), new_positions))
        
# Find trailheads
def find_trailheads(trailmap):
    trailheads = []
    for y_pos, line in enumerate(trailmap):
        for x_pos, el in enumerate(line):
            if el=='0':
                trailheads.append((x_pos, y_pos))
    return trailheads

def find_neighbours_from_trailhead(trailmap, start):
    visited = {start}
    stack = [start]
    while stack:
        current = stack.pop()
        for next in find_traversible_neighbours(current, trailmap):
            if next not in visited:
                visited.add(next)
                stack.append(next)

    return visited

pt1_res = 0
for trailhead in find_trailheads(trailmap):
    traversible_positions = find_neighbours_from_trailhead(trailmap, trailhead)
    found_9s = sum(map(lambda pos: trailmap[pos[1]][pos[0]] == '9', traversible_positions))
    pt1_res += found_9s

print(pt1_res)