# Advent of Code 2
lines = [list(map(int, line.split(" "))) for line in open("input.txt", "r")]

def isDirectional (floors):
    return all([a < b for (a,b) in zip(floors, floors[1:])]) or \
    all([a > b for (a,b) in zip(floors, floors[1:])])

def isGradual (floors):
    return all(1 <= abs(a-b) <= 3 for (a,b) in zip(floors, floors[1:]))

def safetyDampener (floors):
    return any([isDirectional(seq) and isGradual(seq) for seq in removeOne(floors)])

def removeOne(lst):
    return [lst[:i] + lst[i+1:] for i in range(len(lst))]

result1 = sum([isDirectional(seq) and isGradual(seq) for seq in lines])

result2 = sum([safetyDampener(seq) for seq in lines])

print(result1, result2)