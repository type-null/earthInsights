"""
Homework Exercise - SDE in DS Internship
Affinity Solutions

Author: Weihang Ren

"""

import re
from names import STATES, COUNTRIES, BRANDS

def match_brands(tokens: list):
    """
    Mactch tokens to possible brands
    Similarity computed using the Levenshtein distance
    ref: https://www.datacamp.com/community/tutorials/fuzzy-string-python

    """

    brands = {}

    for i in range(len(tokens)):

        brands[f"{i+1}"] = brand

    return brands



def process(description: str):
    """
    Convert input to output format

    """
    # init variables
    state, country, phone_no = "", "", ""

    # clean special characters
    string = re.sub(re.compile(r'[\'*-]+'), ' ', description.lower())

    # tokenize input
    tokens = string.strip().split()

    # classify tokens
    for token in tokens:
        # number
        if token.isnumeric():
            # TODO: will phone_no be other format: 222-222-2222 ?
            phone_no = token
            tokens.remove(token)
        # two character: country or state abbreviation
        elif len(token) == 2:
            if token in COUNTRIES:
                country = token
                tokens.remove(token)
            elif token in STATES.keys():
                state = token
                tokens.remove(token)

    brands = match_brands(tokens)

    output = {
        "brands": [brands],
        "state": state,
        "country": country,
        "phone no": phone_no,
    }

    return output
