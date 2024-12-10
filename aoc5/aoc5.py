# Advent of Code 5
# Author: Daniel Roger Hussey

rules, updates = [], []
sum1, sum2 = 0, 0

def sequence_follows_rule_pair(seq: list, rule_pair):
    return seq.index(rule_pair[0]) < seq.index(rule_pair[1])

# Part 2: Sort a sequence of numbers based on a list of rule pairs when rule_left must come before rule_right
def sort_by_apropos_rule_pairs(seq: list[int], pairs: list[list[int]]):
    rules = {(left, right) for left,right in pairs}
    def compare(a, b):
        if (a,b) in rules:
            return -1
        if (b,a) in rules:
            return 1
    from functools import cmp_to_key
    return sorted(seq, key=cmp_to_key(compare))


for line in  open("input.txt", "r").readlines():
    # Append rule pairs until line is the separator newline
    if len(line.split("|")) == 2:
        rules.append(list(map(int, line.strip().split("|"))))
    elif len(line.split(",")) >= 2:
        updates.append(list(map(int, line.strip().split(","))))

for update_set in updates:
    # Get rules pairs in the rule list whose both members exist in the current update set (e.g 42,43 is included in set 43,43,31,59 as both 42, 43 in that set)
    apropos_rules = list(filter(lambda rule_pair: rule_pair[0] in update_set and rule_pair[1] in update_set, rules))
    if (all([sequence_follows_rule_pair(update_set, rule_pair) for rule_pair in apropos_rules])):
        sum1 += update_set[int((len(update_set)-1)/2)]
    else:
        # Part 2
        reordered_update_set = sort_by_apropos_rule_pairs(update_set, apropos_rules)
        sum2 += reordered_update_set[int((len(reordered_update_set)-1)/2)]


print(sum1)
print(sum2)