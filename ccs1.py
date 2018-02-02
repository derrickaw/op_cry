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
    encoded_base64_str = bytes.decode(base64.b64encode(decoded_hex))

    return encoded_base64_str












if __name__ == '__main__':

    # 1. Convert hex to base64
    assert convert_hex_to_base64('49276d206b696c6c696e6720796f757220627261696e'
                                 '206c696b65206120706f69736f6e6f7573206d757368'
                                 '726f6f6d') \
        == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
