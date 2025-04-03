import csv

def to_gray_code(num):
    """Converts a number to its Gray code representation."""
    return num ^ (num >> 1)

def from_gray_code(gray):
    """Decodes a Gray code number to its original value."""
    num = 0
    while gray:
        num ^= gray
        gray >>= 1
    return num

def binary_to_int(binary_value):
    """Converts a binary string to an integer."""
    return int(binary_value, 2)

def binary_to_bool_list(binary_value, length=18):
    """Converts a binary string to a list of booleans."""
    binary_value = binary_value.zfill(length)  # Ensure correct length
    return [bit == '1' for bit in binary_value]  # Maintain correct order

def pack_bools_to_uint32(bools):
    """Packs a list of booleans into a uint32 integer, matching C++ bit order."""
    result = 0
    for i, val in enumerate(bools):  # Do not reverse bits here
        if val:
            result |= (1 << i)
    return result

def process_csv(file_name):
    """Reads a CSV file, processes binary values, and writes results."""
    output_file = "processed_" + file_name
    
    with open(file_name, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        header = next(reader, None)
        if header:
            writer.writerow(header + ["Decoded Gray Value"])  # Updated header
        
        for row in reader:
            if len(row) < 2:
                continue  # Skip malformed rows
            
            image, binary_value = row
            binary_as_int = binary_to_int(binary_value)
            gray_code = to_gray_code(binary_as_int)
            decoded_value = from_gray_code(gray_code)
            
            bool_list = binary_to_bool_list(binary_value)
            packed_value = pack_bools_to_uint32(bool_list)
            decoded_gray_value = from_gray_code(packed_value)  # Corrected decoding
            
            # Write updated row to CSV
            writer.writerow(row + [decoded_gray_value])

def main():
    process_csv('cleaned_result1.csv')

if __name__ == "__main__":
    main()