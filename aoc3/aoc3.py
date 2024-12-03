memory = "".join([line.strip("\n") for line in open("input.txt", "r")])
pos, sumPart1, sumPart2 = 0,0,0
while (pos := memory.find("mul(", pos)) != -1:
    mul_enabled = memory.rfind("do()", 0, pos) >= memory.rfind("don't()", 0, pos)
    if (rIdx := memory.find(")", pos)) != -1:
        substrs = memory[pos+4:rIdx].split(",")
        if len(substrs)==2 and all(map(str.isnumeric, substrs)):
            sumPart1 += int(substrs[0]) * int(substrs[1])
            if mul_enabled:
                sumPart2 += int(substrs[0]) * int(substrs[1])
        pos+=1
        
print(sumPart1, sumPart2)