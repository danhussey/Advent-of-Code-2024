memory = "".join([line.strip() for line in open("input.txt", "r")])

pos = 0
substrs = []
sum=0
while (pos := memory.find("mul(", pos)) != -1:
    if (rIdx := memory.find(")", pos)) != -1:
        substrs = memory[pos+4:rIdx].split(",")
        if len(substrs)==2 and all(map(str.isnumeric, substrs)):
            sum += int(substrs[0]) * int(substrs[1])            
        pos+=4
print(sum)