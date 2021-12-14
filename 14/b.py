from collections import defaultdict, Counter

with open("input.txt", "r") as f:
    template = f.readline().rstrip()
    f.readline()
    lines = f.read().splitlines()


rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines}


def generate_counts_from_rules(rules, steps):
    counts_by_pair = {pair: Counter(pair) for pair in rules.keys()}
    for _ in range(steps):
        new_counts_by_pair = {}
        for pair, replacement in rules.items():
            char1, char2 = pair
            new_counts = counts_by_pair[char1+replacement] + counts_by_pair[replacement + char2]
            new_counts[replacement] -= 1 # only inserting 1

            new_counts_by_pair[pair] = new_counts
        counts_by_pair = new_counts_by_pair
    return counts_by_pair


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


def calc_frequency(s):
    frequency = Counter()
    for c in s:
        frequency[c] += 1
    return frequency

def update_frequency(s, f):
    for c in s:
        f[c] += 1
    return f

def calc_answer(frequency):
    # most common element quantity - least common quantity
    most_common = max(frequency.values())
    least_common =  min(frequency.values())
    return most_common - least_common

counts_by_pair = generate_counts_from_rules(rules, steps=40)

final_count = Counter()
for i in range(len(template) - 1):
    pair = template[i:i+2]
    final_count += counts_by_pair[pair]

# Every character except the first and last of template are double counted
for i in range(1, len(template)-1):
    final_count[template[i]] -= 1

print(calc_answer(final_count))

