def decode_output(signal_patterns, output):
    inferred_digits = [None for i in range(0, 10)]
    known_seg_len_map = {2: 1, 3: 7, 4: 4, 7: 8}
    combined = signal_patterns + output
    # First do the easy digits
    for s in combined:
        s_len = len(s)
        if s_len in known_seg_len_map:
            inferred_digits[known_seg_len_map[s_len]] = s
    return len([d for d in output if d in inferred_digits])


def sort_string(s):
    """Sort string because segment order doesn't matter"""
    return "".join(sorted(s))


with open("input.txt", "r") as f:
    data = f.read()

lines = data.splitlines()

total_count = 0
for line in lines:
    signal_patterns, output = line.split("|")
    signal_patterns = [sort_string(s) for s in signal_patterns.split()]
    output = [sort_string(s) for s in output.split()]
    count = decode_output(signal_patterns, output)
    total_count += count
print(total_count)
