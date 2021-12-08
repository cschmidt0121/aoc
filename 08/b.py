import itertools

PROPER_SEGMENT_PATTERNS = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6],
}


def string_intersect(s, s2):
    """Return string of chars containing in both s and s2"""
    set1 = set(s)
    set2 = set(s2)
    return "".join(set1.intersection(set2))


def string_difference(s, s2):
    """Return string of chars that are in s and NOT s2"""
    set1 = set(s)
    set2 = set(s2)
    return "".join(set1.difference(set2))


def sort_string(s):
    """Sort string because segment order doesn't matter"""
    return "".join(sorted(s))


def validate_digit(s, assumed_segment_numbers):
    """
    With a set of assumed segment letters, test if a set of enabled wires could
    possibly represent a number
    """
    len_s = len(s)

    # Brain fried
    resolved_segment_patterns = {
        k: sort_string("".join([assumed_segment_numbers[i] for i in v]))
        for k, v in PROPER_SEGMENT_PATTERNS.items()
    }
    # 0, 6, or 9
    if len_s == 6:
        for segment in s:
            if segment not in "".join(
                [
                    resolved_segment_patterns[0],
                    resolved_segment_patterns[6],
                    resolved_segment_patterns[9],
                ]
            ):
                return False
    # 2, 3, or 5
    elif len_s == 5:
        for segment in s:
            if segment not in "".join(
                [
                    resolved_segment_patterns[2],
                    resolved_segment_patterns[3],
                    resolved_segment_patterns[5],
                ]
            ):
                return False
    return True


def validate_output(output, assumed_segment_numbers):
    resolved_segment_patterns = {
        sort_string("".join([assumed_segment_numbers[i] for i in v])): k
        for k, v in PROPER_SEGMENT_PATTERNS.items()
    }

    result = 0
    for i, digit in enumerate(output):
        try:
            result += (10 ** (len(output) - i - 1)) * resolved_segment_patterns[digit]
        except KeyError:
            return False
    return result


def decode_output(signal_patterns, output):
    inferred_digits = [None for i in range(0, 10)]
    known_seg_len_map = {2: 1, 3: 7, 4: 4, 7: 8}
    combined = signal_patterns + output
    # First do the easy digits
    for s in combined:
        s_len = len(s)
        if s_len in known_seg_len_map:
            inferred_digits[known_seg_len_map[s_len]] = s
    # On a properly functioning display, segment 0==a, 1==b, etc
    # For each segment, possible_segment_letters contains the letters that could possibly represent it
    possible_segment_letters = ["abcdefg" for i in range(0, 7)]

    # Now make some logical conclusions about which segment is which
    # The only one we can definitively nail down is segment 0, if we know what segments make up 7 and 1
    if inferred_digits[1]:
        possible_segment_letters[2] = inferred_digits[1][0] + inferred_digits[1][1]
        possible_segment_letters[5] = inferred_digits[1][0] + inferred_digits[1][1]

    if inferred_digits[4]:
        if inferred_digits[1]:
            possible_segment_letters[1] = string_difference(
                inferred_digits[4], inferred_digits[1]
            )
            possible_segment_letters[3] = string_difference(
                inferred_digits[4], inferred_digits[1]
            )
        elif inferred_digits[7]:
            possible_segment_letters[1] = string_difference(
                inferred_digits[4], inferred_digits[7]
            )
            possible_segment_letters[3] = string_difference(
                inferred_digits[4], inferred_digits[7]
            )
        else:
            possible_segment_letters[1] = inferred_digits[4]
            possible_segment_letters[2] = inferred_digits[4]
            possible_segment_letters[3] = inferred_digits[4]
            possible_segment_letters[5] = inferred_digits[4]

    if inferred_digits[7]:
        if inferred_digits[1]:
            possible_segment_letters[0] = string_difference(
                inferred_digits[7], inferred_digits[1]
            )
        elif inferred_digits[4]:
            possible_segment_letters[0] = string_difference(
                inferred_digits[7], inferred_digits[4]
            )
        else:
            possible_segment_letters[0] = (
                inferred_digits[7][0] + inferred_digits[7][1] + inferred_digits[7][2]
            )
            possible_segment_letters[2] = (
                inferred_digits[7][0] + inferred_digits[7][1] + inferred_digits[7][2]
            )
            possible_segment_letters[5] = (
                inferred_digits[7][0] + inferred_digits[7][1] + inferred_digits[7][2]
            )

    # Ok, I've narrowed it down as much as I can so now I guess and check the rest
    assumed_segment_letters_permutations = [
        "".join(s) for s in itertools.product(*possible_segment_letters)
    ]
    for p in assumed_segment_letters_permutations:
        # Skip permutations where the same segment is assigned to multiple letters or no letters
        if (
            "a" not in p
            or "b" not in p
            or "c" not in p
            or "d" not in p
            or "e" not in p
            or "f" not in p
            or "g" not in p
        ):
            continue
        contradiction = False
        for digit in combined:
            # First validate individual digits in the output
            valid = validate_digit(digit, p)
            if not valid:
                contradiction = True
        if not contradiction:
            # If all the digits make sense, then validate the output as a whole
            total = validate_output(output, p)
            if total:
                # Proper layout found!
                return total
            else:
                contradiction = True

    if not total:
        print("Couldn't find a solution")
        return


with open("input.txt", "r") as f:
    data = f.read()

lines = data.splitlines()

total_count = 0
for line in lines:
    signal_patterns, output = line.split("|")
    signal_patterns = [sort_string(s) for s in signal_patterns.split()]
    output = [sort_string(s) for s in output.split()]
    total_count += decode_output(signal_patterns, output)

print(total_count)
