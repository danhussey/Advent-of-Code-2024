def get_xmas_strings(grid, row, col, length=4, diagonal=True):
    rows, cols = len(grid), len(grid[0])
    strings = []
    
    directions = [
        (-1, 0),   # up
        (0, 1),    # right
        (1, 0),    # down
        (0, -1),   # left
        (-1, 1),   # top-right
        (1, 1),    # bottom-right
        (1, -1),   # bottom-left
        (-1, -1)   # top-left
        ]
    
    for dr, dc in directions:
        current_string = []
        current_path = []
        
        for step in range(length):
            new_row = row + (dr * step)
            new_col = col + (dc * step)
            
            if 0 <= new_row < rows and 0 <= new_col < cols:
                current_string.append(str(grid[new_row][new_col]))
                current_path.append((new_row, new_col))
            else:
                break
        
        if len(current_string) == length:
            string = ''.join(current_string)
            if string == 'XMAS':
                strings.append({
                    'string': string,
                    'path': current_path
                })
    
    return strings

def scan_grid(grid, length=4, diagonal=True):
    rows, cols = len(grid), len(grid[0])
    all_strings = []
    
    for row in range(rows):
        for col in range(cols):
            strings = get_xmas_strings(grid, row, col, length, diagonal)
            all_strings.extend(strings)
    
    return all_strings

crossword = [line.strip() for line in open("input.txt", "r")]

print(len(scan_grid(crossword)))