from collections import defaultdict

with open("input.txt", "r") as f:
    template = f.readline().rstrip()
    f.readline()
    lines = f.read().splitlines()


rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines}

def do_replacement(s, rules):
    replacements = [] # index, value
    for i in range(0, len(s)-1):
        pair = s[i:i+2]
        if pair in rules.keys():
            replacements.append([i+1, rules[pair]])

    replacements = sorted(replacements, reverse=True)
    for index, value in replacements:
        s = s[:index] + value + s[index:]
    return s

def calc_answer(s):
    # most common element quantity - least common quantity
    elements = defaultdict(int)
    for c in s:
        elements[c] += 1
    most_common = elements[max(elements, key=elements.get)]
    least_common = elements[min(elements, key=elements.get)]
    return most_common - least_common


s = template
for i in range(0, 10):
    s = do_replacement(s, rules)
print(calc_answer(s))

