
with open("input_sample.txt", "r") as f:
    data=f.read()

bytes = bytearray.fromhex(data)
current_bit = 0

masks ={1: 0x80,
         2: 0xc0,
         3: 0xe0,
         4: 0xf0,
         5: 0xf8,
         6: 0xfc,
         7: 0xfe,
         8: 0xff}

high_masks = {1: 0x01, 2:0x03, 3:0x07, 4:0x15, 5:0x31}

def read_bits(num_bits):
    global current_bit
    global bytes
    if current_bit + num_bits <= 8:
        byte = bytes[0]
        byte = byte << current_bit
        mask = masks[num_bits]
        current_bit += num_bits
        if current_bit == 8:
            print("wrapping")
            bytes = bytes[1:]
            current_bit = 0
        return (byte & mask) >> (8-num_bits)
    else:
        byte = bytes[0]\
        high_bits = (byte & high_masks[8-current_bit])
        shift_amount = 8-current_bit
        num_bits -= 8-current_bit
        bytes = bytes[1:]
        current_bit = 0
        byte = bytes[0]
        mask = masks[num_bits]
        current_bit += num_bits\
        return ((byte & mask) >> (8 - num_bits)) | (high_bits << shift_amount)

def read_literal():
    literal_value = 0

    while True:
        continue_reading = read_bits(1)
        print("continue")
        print(continue_reading)
        literal_bits = read_bits(4)
        print("literal")
        print(literal_bits)
        literal_value = (literal_value << 4) | literal_bits
        if not continue_reading == 1:
            break
    return literal_value

packet_version = read_bits(3)
packet_type = read_bits(3)
print(packet_version)
print(packet_type)

if packet_type == 4:
    print(read_literal())