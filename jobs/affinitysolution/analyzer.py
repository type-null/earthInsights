"""
Homework Exercise - SDE in DS Internship
Affinity Solutions

Author: Weihang Ren

"""

import re
import json
import numpy as np
from names import STATES, COUNTRIES, BRANDS

def similarity(token, brand):
    """
    Return most possible brand for given token
    Similarity computed using the Levenshtein distance
    ref: https://www.datacamp.com/community/tutorials/fuzzy-string-python

    """
    # Initialize matrix of zeros
    rows = len(token)+1
    cols = len(brand)+1
    distance = np.zeros((rows, cols), dtype=int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if token[row-1] == brand[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                cost = 2
            distance[row][col] = min(distance[row-1][col] + 1,          # Cost of deletions
                                     distance[row][col-1] + 1,          # Cost of insertions
                                     distance[row-1][col-1] + cost)     # Cost of substitutions

    return ((len(token)+len(brand)) - distance[row][col]) / (len(token)+len(brand))



def process(description: str):
    """
    Convert input to output format

    """
    # init variables
    state, country, phone_no = "", "", ""

    # clean special characters
    string = re.sub(re.compile(r'[\'*-]+'), '', description.lower())

    # tokenize input
    tokens = string.strip().split()

    # classify tokens
    tokens_used = []
    for token in tokens:
        # number
        if token.isnumeric():
            # TODO: will phone_no be in other format: 222-222-2222 ?
            phone_no = token
            tokens_used.append(token)
        # two character: country or state abbreviation
        elif len(token) == 2:
            if token in COUNTRIES:
                country = token
                tokens_used.append(token)
            elif token in STATES.keys():
                state = token
                tokens_used.append(token)

    tokens_remain = [t for t in tokens if t not in tokens_used]
    # match rest tokens to brands
    brands = {}

    for i in range(len(tokens_remain)):
        if tokens_remain[i] in BRANDS:
            brand = tokens_remain[i]
        else:
            probability = {brand: similarity(brand, tokens_remain[i]) for brand in BRANDS}
            brand_guess = sorted([(p, b) for b, p in probability.items()], reverse=True)
            brand_guess = [b for _, b in brand_guess]
            brand = brand_guess[0]

        brands[f"{i+1}"] = brand

    data = {
        "brands": [brands],
        "state": state,
        "country": country,
        "phone no": phone_no,
    }

    return json.dumps(data)
