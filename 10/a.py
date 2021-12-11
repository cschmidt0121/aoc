with open("input.txt", "r") as f:
    lines = f.read().splitlines()

valid_pairs={'{': '}', '(': ')', '[': ']', '<': '>'}

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
total_score = 0
for line in lines:
    chunk_stack = []
    for c in line:
        if c in valid_pairs.keys():
            chunk_stack.append(c)
        else:
            current_chunk = chunk_stack.pop()
            if c != valid_pairs[current_chunk]:
                total_score += scores[c]
                break

print(total_score)