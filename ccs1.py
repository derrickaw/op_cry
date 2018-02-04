# Cryto Challenge Set 1
"""
1. Convert hex to base64


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
    encoded_base64_str = base64.b64encode(decoded_hex) # bytes.decode(base64.b64encode(decoded_hex))
    print(encoded_base64_str)
    return encoded_base64_str


def xor_fixed_buffers(buf1, buf2):

    buf1_base64 = convert_hex_to_base64(buf1)
    buf2_base64 = convert_hex_to_base64(buf2)

    xor_buf_ba = bytearray(len(buf1))
    #buf1_base64_ba = bytearray(buf1_base64)
    #buf2_base64_ba = bytearray(buf2_base64)

    for i in range(len(len(buf1_base64))):
        xor_buf_ba[i] = buf1_base64[i] ^ buf2_base64[i]

    return xor_buf_ba












if __name__ == '__main__':

    # 1. Convert hex to base64
    assert bytes.decode(convert_hex_to_base64('49276d206b696c6c696e6720796f757'
                                              '220627261696e206c696b6520612070'
                                              '6f69736f6e6f7573206d757368726f6'
                                              'f6d')) \
        == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    # 2. Fixed XOR
    assert xor_fixed_buffers('1c0111001f010100061a024b53535009181c',
                             '686974207468652062756c6c277320657965') \
           == '746865206b696420646f6e277420706c6179'
