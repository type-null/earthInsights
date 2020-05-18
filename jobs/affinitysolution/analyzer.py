"""
Homework Exercise - SDE in DS Internship
Affinity Solutions

Author: Weihang Ren

"""

import re
from names import STATES, COUNTRIES, BRANDS

def process(description):
    """
    Convert input to output format

    """

    # clean special characters
    string = re.sub(re.compile(r'[\'*-]+'), ' ', description.lower())

    # tokenize input
    tokens = string.strip().split()

    # classify tokens
    for token in tokens:
        # number
        if token.isnumeric():
            # TODO: will the phone no in other format: 222-222-2222 ?
            phone_no = token
        # two character: country or state abbreviation
        elif len(token) == 2:
            if token in COUNTRIES:
                country = token
            elif token in STATES.keys():
                state = token
            continue

    brands = match_brands(tokens_remain)

    # init output
    output = {
        "brands": [brands],
        "state": state,
        "country": country,
        "phone no": phone_no,
    }

    return output
