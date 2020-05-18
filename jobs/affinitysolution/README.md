# Homework Exercise - SDE in DS Internship
Weihang Ren
May 18, 2020

## Files
- **analyzer.py**: main functions
    - `similarity()` calculate the Levenshtein distance between two strings
    - `process()` takes input string and output required json

- **analyzer_test.py**: tests the `analyzer.process()` for each input and output pair in the given dataset

- **names.py**: contains STATES, COUNTRIES, BRANDS lists for looking up

- **data.xlsx**: given dataset, originally named **Home Work Exercise - Software Development Engineer in DS - Intern.xlsx**

## Explaination of `analyzer.process()`

1. clean special characters (`[\'*-]`) from the input

2. tokenize input

3. classify each token
    1. if token is a number -> **"ph no"**
      (need to change there other formats of possible phone number input)

    2. else if token is a 2-letter string
      - if in COUNTRIES list (i.e., == "us") -> **"country"**
      - if in STATES list -> **"state"**

    3. else calculate the similarity (the Levenshtein distance) between the token and each brand in BRANDS list and then assign the most similar brand to that token as a part of **"brand"**

4. format output

## The Levenshtein Distance
Reference: [here](https://www.datacamp.com/community/tutorials/fuzzy-string-python)
