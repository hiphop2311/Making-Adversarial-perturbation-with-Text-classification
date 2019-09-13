import os
import preprocess
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
root_path = '/Users/thanathip/Desktop/Assignment/News classification'
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

data = pd.read_csv(os.path.join(root_path,"data.csv"))

data['content'] = data['content'].map(preprocess.clean_txt)
X_train, X_test, y_train, y_test = train_test_split(
    data['content'],
    data['label'],
    test_size = 0.2,
    random_state=1,
    stratify=data['label']
)

news_clf = Pipeline([('vect', CountVectorizer()),
 ('tfidf', TfidfTransformer()),
 ('clf-NB', MultinomialNB())])

news_clf.fit(X_train, y_train)
predicted = news_clf.predict(X_test)

joblib.dump(news_clf, os.path.join(root_path,"NB_MTNB.pkl")) 
