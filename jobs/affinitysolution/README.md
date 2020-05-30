# Homework Exercise - SDE in DS Internship

Weihang Ren

May 18, 2020

## Files
- **analyzer.py**: main functions
    - `similarity()` calculate the Levenshtein similarity ratio between two strings
    - `process()` takes input string and output required json

- **analyzer_test.py**: tests the `analyzer.process()` for each input and output pair in the given dataset

- **names.py**: contains STATES, COUNTRIES, BRANDS lists for looking up

- **data.xlsx**: given dataset, originally named **Home Work Exercise - Software Development Engineer in DS - Intern.xlsx**

## Explaination of `analyzer.process()`

1. clean special characters (`[\'*-]`) from the input

2. tokenize input

3. classify each token
    1. if token is a number -> **"ph no"**
      (need to change if there are other formats of possible phone number input)

    2. else if token is a 2-letter string
        - if in COUNTRIES list (i.e., == "us") -> **"country"**
        - if in STATES list -> **"state"**

    3. else calculate the similarity (the Levenshtein distance) between the token and each brand in BRANDS list and then assign the most similar brand to that token as a part of **"brand"**

4. format output

## Explaination of `analyzer.similarity()`
Reference: [The Levenshtein Similarity Ratio](https://www.datacamp.com/community/tutorials/fuzzy-string-python)

Use dynamic programming to calculate the Levenshtein distance matrix for "paypal" and "payal":

| | |**p**|**a**|**y**|**p**|**a**|**l**|
|-|-|-|-|-|-|-|-|
| |0|1|2|3|4|5|6|
|**p**|1|0|1|2|3|4|5|
|**a**|2|1|0|1|2|3|4|
|**y**|3|2|1|0|1|2|3|
|**a**|4|3|2|1|2|1|2|
|**l**|5|4|3|2|3|2|**1**|

Then the similarity ratio is calculated by
$$\frac{|paypal|+|payal|-1}{|paypal|+|payal|} = 90.9\%$$
