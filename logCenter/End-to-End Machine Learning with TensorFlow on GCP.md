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
    <img src="https://i.imgur.com/Hz5xw0x.png" width=700 alt="AI Platform NB">
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
<img src="https://i.imgur.com/Tw47UTC.png" width=500 alt="bq-output">

### Lab 1
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

To work on a smaller sample before scale it on the cloud, change the last line to
```mysql
WHERE
    MOD(ABS(FARM_FINGERPRINT(data)), 10) < 8 AND RAND() < 0.01
```

### Lab 2
**training-data-analyst > courses > machine_learning > deepdive > 06_structured > labs** and open **2_sample.ipynb**.

## Build the model
A tensor is an n-dimensional array of data. Your data flows through the graph, hence Tensorflow.
<img src="https://i.imgur.com/1MNiFRn.png" width=700 alt='tensor'>

### Working with estimator API

1. Set up machine learning model
  - Regression or classification?
  - What is the label?
  - What are the features?

2. Carry out ML steps
  - Train the model
  - Evaluate
  - Predict with the model

<img src="https://i.imgur.com/3xtNdA7.png" width=700 alt='Estimator API'>

### Encoding categorical data to supply to a DNN

1a. If you know the complete vocabulary beforehand;
```python
tf.feature_column.categorical_column_with_vocabulary_list('zipcode',
    vocabulary_list=['83452', '72345', '87654', '23451'])
```

1b. If your data is already indexed; i.e., has integers in \[0,N):
```python
tf.feature_column.categorical_column_with_identity('stateId',
    num_buckets=50)
```

Then,

2. To pass in a categorical column into a DNN, one option is to one-hot encode it (to make a sparse column dense):
```python
tf.feature_column.indicator_column( my_categorical_column )
```

or use an embedding column.

### Bucketize numeric features
```python
mother_age = tf.feature_column.numeric_column('mother_age')
age_buckets = tf.feature_column.bucketized_column(mother_age,
    boundaries=np.arange(15,45,1).tolist())
```

### To read CSV files
create a TextLineDataset giving it a function to decode CSV into features, labels.

```python
CSV_COLUMNS = ['sqfootage', 'city', 'amount']
LABEL_COLUMN = 'amount'
DEFAULTS = [[0.0], 'na', [0.0]]

def read_dataset(filename, mode, batch_size=512):
    def decode_csv(value_column):
        columns = tf.decode_csv(value_column, record_defaults=DEFAULTS)
        features = dict(zip(CSV_COLUMNS, columns))
        label = features.pop(LABEL_COLUMN)
        return features, label

    dataset = tf.TextLineDataset(filename).map(decode_csv)

    # Shuffling is important for distributed training
    if mode == tf.estimator.ModeKeys.TRAIN:
        num_epochs = None # indefinitely
        dataset = dataset.shuffle(buffer_size=10*batch_size)
    else: # we are evaluating
        num_epochs = 1 # end-of-input after this
    dataset = dataset.repeat(num_epochs).batch(batch_size)

    return dataset.make_one_shot_iterator().get_next()
```

### Train and eval together

<img src="https://i.imgur.com/rpdPVqu.png" width=700 alt="train and evaluate">
<img src="https://i.imgur.com/zHV8HQH.png" width=700 alt="train specs">
<img src="https://i.imgur.com/S7hIHK6.png" width=700 alt="train specs">


### Creating a TensorFlow model

Two types of features: Dense and Sparse
  - DNNs good for dense, highly-correlated inputs
    - image pixels
  - Linear models are better at handling sparse, independent features

Wide-and-deep models let you handle both.
  - memorization -> relevance
  - generalization -> diversity
<img src="https://i.imgur.com/qRPp8C8.png" width=700 alt="wide&deep">

Wide-and-deep network in Estimator API:
```python
model = tf.estimator.DNNLinearCombinedClassifier(
    model_dir=...,
    linear_feature_columns=wide_columns,
    dnn_feature_columns=deep_columns,
    dnn_hidden_units=[100,50])
```

