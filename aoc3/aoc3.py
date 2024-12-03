memory = "".join([line.strip() for line in open("input.txt", "r")])

lIdx = 0
rIdx = 0
substrs = []
sum=0
while rIdx != -1:
    lIdx = memory.find("mul(", lIdx)
    rIdx = memory.find(")", lIdx)
    if rIdx != -1:
        substr = memory[lIdx+4:rIdx]
        print(substr)
        if len(substr.split(",")) == 2 and all(map(str.isnumeric, substr.split(","))):
            sum += int(substr.split(",")[0])*int(substr.split(",")[1])
        lIdx+=4


print(sum)