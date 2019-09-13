# Making-Adversarial-perterbation-for-Text-classification
# Dataset

* Consists of 2225 documents from the [BBC](http://mlg.ucd.ie/datasets/bbc.html) news website corresponding to stories in five topical areas from 2004-2005.
* Class Labels: 5 (business, entertainment, politics, sport, tech)

# Classification model using

* Multinomial Naive Baye

# Preprocessing

* Convert all letter to lower case
* Remove punctuation
* Tokenize word
* Remove stopwords
* Remove stopwords
* Lemmatize

# Make perturbation

* Random swap characters in each significant word collected from training Corpus (others are applied with fix probability )

* Change some characters to a similar one.

* Dropout some frequent words.

## Run



```bash
python3 controller.py
```

## Result

| Input        | Accuracy      | F1   |
| ------------- |:-------------:| -----: |
| News report     |  0.964 |0.963
| News report with perturbation |0.424 |0.396


## Example program

![Image description](https://github.com/hiphop2311/Making-Adversarial-perturbation-for-Text-classification/blob/master/example.png)
