disk_map = open("aoc9/input.txt", "r").readline().strip()
disk = []
# Get the hard drive file representation
for index in range(len(disk_map)):
    if index % 2 == 0:
        # File length number
        disk.extend([int(index/2)]*int(disk_map[index]))
    else:
        # Blank space length number
        disk.extend([None]*int(disk_map[index]))

def is_compacted(disk):
    return all(map(lambda x: x is None, disk[disk.index(None):]))

first_empty_space_index = 0
rightmost_val_index = len(disk)-1
while(is_compacted(disk) is not True):
    first_empty_space_index = disk.index(None, first_empty_space_index)
    for i in range(rightmost_val_index-1, -1, -1):
        if disk[i] != None: 
            rightmost_val_index = i
            break

    disk[first_empty_space_index] = disk[rightmost_val_index]
    disk[rightmost_val_index] = None

# Calculate checksum sum(index * id)
checksum_pt_1 = sum([index * id if id is not None else 0 for index, id in enumerate(disk)])
print(checksum_pt_1)
