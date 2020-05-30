# Week1

## Effective ML

<p align='center'>
    <img src='https://i.imgur.com/QISF1Mn.png' width=500 alt='Tensorflow with GMLE'/>
    <img src='https://i.imgur.com/7zsdIcN.png' width=700 alt='ML Process'/>
</p>

## Big Query

<p align='center'>
    <img src='https://i.imgur.com/ccSpJfJ.png' width=400 alt='Big Query'/>
    <img src='https://i.imgur.com/7llz2qW.png' width=500 alt='Big Query UI'/>
</p>

AI Platform Notebooks work with the same technologies that you’re comfortable with, so you can start developing now, and then work on scale later. For example, we’ll be doing an exercise where we read from a .csv file. You could then process in Pandas and Apache Beam before training a model in TensorFlow, and then improve the model through training.

<p align="center">
    <img src="https://i.imgur.com/Hz5xw0x.png" width=450 alt="AI Platform NB">
</p>

### Big Query in Python to get a Pandas DF

```python
query = """
SELECT
    weight_pounds,
    is_male,
    mother_age,
    popularity,
    gestation_weeks,
    ABS(FARM_FINGERPRINT(CONCAT(CAST(YEAR AS STRING), CAST(month AS STRING)))) AS hashmonth
FROM
    publicdata.samples.natality
WHERE year > 2000
"""

# Call BigQuery and examine in dataframe
import google.datalab.bigquery as bq 
df = bg.Query(query + " LIMIT 100").execute().result().to_dataframe()
df.head()
```
Output:
<img src="https://i.imgur.com/Tw47UTC.png" width=400 alt="bq-output">

## Lab 1
**training-data-analyst > courses > machine_learning > deepdive > 06_structured > labs** and open **1_explore.ipynb**.

# Week2

## Create a dataset

### What makes a dataset "good"?

1. Be related to the objective
2. Be known at prediction-time
3. Be numeric with meaningful magnitude
4. Have enough examples for different features
5. Human indight (domain knowledge)


### How to deal with triplet data?
Three identical rows should be treated as a single record.

<img src="https://i.imgur.com/9bjyZE7.png" width="600" alt="solution">



