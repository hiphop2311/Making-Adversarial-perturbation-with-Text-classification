import numpy as np
import pandas as pd
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re


nltk.download('stopwords')
nltk.download('wordnet')
class preprocessText():

    def __init__(self):
        self.stops = set(stopwords.words("english"))
        self.wordnet_lemmatizer = WordNetLemmatizer()
        self.new_text = ""
    def clean_txt(self,text):
        """to lowercase"""
        # new_text = text.encode("ascii","ignore")
        self.new_text = text.lower()

        """remove number"""
        self.new_text = re.sub(r'\d+', '', self.new_text)
        """remove puctuation >> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
        self.new_text = re.sub("["+string.punctuation+"]", " ", self.new_text)

        """remove stop word """
        self.new_text = self.rm_stopwords(self.new_text)

        """Lemmatization """
        self.new_text = self.to_rootwords(self.new_text)
        return self.new_text

    def rm_stopwords(self,text):
        self.text_rm = text
        self.text_rm = [word for word in self.text_rm.split() if word not in self.stops]
        return " ".join(self.text_rm)


    def to_rootwords(self,text):
        self.text_rw = text
        self.text_rw = [self.wordnet_lemmatizer.lemmatize(word, pos="v") for word in text.split()]
        return " ".join(self.text_rw)
