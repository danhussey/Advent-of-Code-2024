memory = "".join([line.strip() for line in open("input.txt", "r")])

lIdx = 0
rIdx = 0
substrs = []
sum=0
while rIdx != -1:
    lIdx = memory.find("mul(", lIdx)
    rIdx = memory.find(")", lIdx)
    if rIdx != -1:
        substrs = memory[lIdx+4:rIdx].split(",")
        if len(substrs)==2 and all(map(str.isnumeric, substrs)):
            sum += int(substrs[0]) * int(substrs[1])            
        lIdx+=4
print(sum)