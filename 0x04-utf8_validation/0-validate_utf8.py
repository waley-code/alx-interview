#!/usr/bin/python3
"""
    a method that determines if a given data set represents
    a valid UTF-8 encoding.
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
"""


def validUTF8(data):
    """
        determines if a given data set represents a valid UTF-8 encoding
    """

    def is_valid_subsequent(byte):
        """
            Helper function to check if subsequent bytes start with "10"
        """
        return (byte >> 6) == 0b10

    remaining_bytes = 0

    for byte in data:
        """Get the 8 least significant bits of the byte"""
        byte = byte & 0xFF

        if remaining_bytes == 0:
            # If the byte starts with "0", it's a single-byte (1 byte)
            if (byte >> 7) == 0b0:
                remaining_bytes = 0
            # If the byte starts with "110", it's a two-byte  (2 bytes)
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1
            # If the byte starts with "1110", it's a three-byte  (3 bytes)
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            # If the byte starts with "11110", it's a four-byte  (4 bytes)
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                # Invalid UTF-8 start byte
                return False
        else:
            # Check if subsequent bytes start with "10"
            if not is_valid_subsequent(byte):
                return False

            remaining_bytes -= 1

    # All s in the list form a valid UTF-8 encoding
    return remaining_bytes == 0
