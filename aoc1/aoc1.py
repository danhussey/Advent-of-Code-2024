# Read text input file
list1, list2 = [], []
with open("input.txt") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1, list2 = sorted(list1), sorted(list2)

# Part 1 , distance score
distance_score = [abs(a - b) for a,b in zip(list1, list2)]

# Part 2, similarity score
similarity_score = sum([x*list2.count(x) for x in list1])