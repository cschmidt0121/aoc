with open("input.txt", "r") as f:
    lines = f.read().splitlines()

valid_pairs={'{': '}', '(': ')', '[': ']', '<': '>'}

score_lookup = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []
for line in lines:
    chunk_stack = []
    corrupted=False
    for c in line:
        if c in valid_pairs.keys():
            chunk_stack.append(c)
        else:
            current_chunk = chunk_stack.pop()
            if c != valid_pairs[current_chunk]:
                corrupted=True
                break
    if corrupted:
        continue
    new_line = line
    total_score = 0
    while len(chunk_stack)>0:
        current_chunk = chunk_stack.pop()
        new_line += valid_pairs[current_chunk]
        total_score = (total_score*5) + score_lookup[valid_pairs[current_chunk]]
    scores.append(total_score)

scores = sorted(scores)
print(scores[(int(len(scores)/2))])