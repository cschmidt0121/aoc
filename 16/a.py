with open("input.txt", "r") as f:
    data = f.read()

bytes = bytearray.fromhex(data)
current_bit = 0
version_sum = 0

masks = {
    1: 0x80,
    2: 0xC0,
    3: 0xE0,
    4: 0xF0,
    5: 0xF8,
    6: 0xFC,
    7: 0xFE,
    8: 0xFF,
    14: 0xFFFC,
}

high_masks = {1: 0x01, 2: 0x03, 3: 0x07, 4: 0xF, 5: 0x1F, 6: 0x3F, 7: 0x7F, 8: 0xFF}


def read_bits(num_bits):
    global current_bit
    global bytes
    if current_bit + num_bits <= 8:
        byte = bytes[0]
        byte = byte << current_bit
        mask = masks[num_bits]
        current_bit += num_bits
        if current_bit == 8:
            bytes = bytes[1:]
            current_bit = 0
        return (byte & mask) >> (8 - num_bits)
    else:
        byte = bytes[0]
        high_bits = byte & high_masks[8 - current_bit]
        # shift_amount = 8 - current_bit
        num_bits -= 8 - current_bit
        bytes = bytes[1:]
        current_bit = 0
        while num_bits > 8:
            byte = bytes[0]
            high_bits = byte | (high_bits << 8)
            bytes = bytes[1:]
            num_bits -= 8

        byte = bytes[0]
        mask = masks[num_bits]
        current_bit += num_bits
        if current_bit == 8:
            bytes = bytes[1:]
            current_bit = 0
        return ((byte & mask) >> (8 - num_bits)) | (high_bits << num_bits)


def read_literal():
    literal_value = 0

    while True:
        continue_reading = read_bits(1)
        literal_bits = read_bits(4)
        literal_value = (literal_value << 4) | literal_bits
        if not continue_reading == 1:
            break
    return literal_value


def handle_operator():
    length_type_id = read_bits(1)
    if length_type_id == 0:
        total_length_in_bits = read_bits(15)
        num_sub_packets = int(total_length_in_bits / 11)
        remainder = total_length_in_bits - (11 * num_sub_packets)
    elif length_type_id == 1:
        num_sub_packets = read_bits(11)
        remainder = 0
    current_subpacket = 0
    subpackets = []
    while True:
        if current_subpacket == (num_sub_packets - 1):
            if remainder > 0:
                parse_packet()

            break
        else:
            parse_packet()
            current_subpacket += 1


def parse_packet():
    global version_sum
    packet_version = read_bits(3)
    version_sum += packet_version
    packet_type = read_bits(3)
    if packet_type == 4:
        literal = read_literal()
    else:
        handle_operator()


while True:
    if len(bytes) == 0:
        break
    try:
        parse_packet()
    except IndexError:
        break

print(version_sum)
