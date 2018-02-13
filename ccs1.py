# Crypto Challenge Set 1
"""
1. Convert hex to base64
2. Fixed buffer XOR
3.

"""

import base64


def convert_hex_to_base64(hex):
    """
    Converts hex string to base64 encoding
    :param hex: hex encoded string
    :return: base64 encoded string
    """
    # Convert hex to byte string
    decoded_hex = bytearray.fromhex(hex)

    # Convert byte string to base64 encoded string; then convert to string
    encoded_base64_str = bytes.decode(base64.b64encode(decoded_hex))

    return encoded_base64_str


def xor_fixed_buffers(buf1, buf2):
    """
    Creates XOR buffered string from two hex string buffers
    :param buf1: hex encoded string
    :param buf2: hex encoded string
    :return: xor hex encoded string
    """

    # Convert hex to bytearray
    decoded_hex_buf1 = bytearray.fromhex(buf1)
    decoded_hex_buf2 = bytearray.fromhex(buf2)

    # XOR by byte
    xor_buf = bytearray(len(decoded_hex_buf1))

    for i in range(len(xor_buf)):
        xor_buf[i] = decoded_hex_buf1[i] ^ decoded_hex_buf2[i]

    # Convert back to hex string
    xor_buf = bytes(xor_buf).hex()

    return xor_buf












if __name__ == '__main__':

    # 1. Convert hex to base64
    assert convert_hex_to_base64('49276d206b696c6c696e6720796f757'
                                 '220627261696e206c696b6520612070'
                                 '6f69736f6e6f7573206d757368726f6'
                                 'f6d') \
        == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    # 2. Fixed XOR
    assert xor_fixed_buffers('1c0111001f010100061a024b53535009181c',
                             '686974207468652062756c6c277320657965') \
           == '746865206b696420646f6e277420706c6179'
