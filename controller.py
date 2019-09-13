
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QStandardItemModel
from ui import Ui_MyApp
from preprocess import preprocessText
from sklearn.externals import joblib
from nltk.corpus import stopwords
import re,random,string
import pandas as pd
import pickle
# from PyQt5 import QtCore, QtGui, QtWidgets
class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MyApp()
        self.ui.setupUi(self)
        self.classifier = joblib.load('./model/NB001.pkl')
        self.category = ['politics','business','entertainment','sport','tech']
        with open("./freq_word.pickle","rb") as file:
            self.freq_word = pickle.load(file)
        with open("./non_ascii.pickle","rb") as file:
            self.non_ascii_char = pickle.load(file)
        self.sig_word  = self.filterFreqWord(self.freq_word,50)

        self.preprocess = preprocessText()
        self.ui.selectFileButton.clicked.connect(self.insertText)
        self.ui.predictButton_1.clicked.connect(self.rawNewsResult)
        self.ui.predictButton_2.clicked.connect(self.perturbedNewsResult)
        self.ui.perturbTextButton.clicked.connect(self.makePerturbation)
    def getFilePath(self):
        self.filePath,_=QFileDialog.getOpenFileName(self,'PATH','./','*.txt')
        return self.filePath
    def insertText(self):
        """insert path"""
        self.ui.linePath.setText(self.getFilePath())

        """insert text in box"""
        with open(self.filePath,"rb") as f:
            self.data = f.read().decode('utf-8','ignore')
            self.ui.plainTextEdit_2.setPlainText(self.data)
        return
    def filterFreqWord(self,freq_word,min_freq):
        self.word_list = []
        for key in freq_word.keys():
            if freq_word[key] > min_freq:
                self.word_list.append(key)
        print(self.word_list)
        return self.word_list
    def predict(self,text_):
        self.preprocessed_text = self.preprocess.clean_txt(text_)
        print(self.preprocessed_text)
        self.preprocessed_text_pd = pd.Series([self.preprocessed_text])
        self.predictions = self.classifier.predict(self.preprocessed_text_pd)
        print(self.predictions)
        return self.category[self.predictions[0]]

    def rawNewsResult(self):
        text = self.ui.plainTextEdit_2.toPlainText()
        self.prediction2 = self.predict(text)

        # print(self.prediction2)
        self.ui.label_predict_1.setText("Result: " + self.prediction2)
        return
    def perturbedNewsResult(self):

        self.prediction3 = self.predict(self.ui.plainTextEdit_3.toPlainText())
        # print(self.ui.plainTextEdit_3.toPlainText())
        self.ui.label_predict_2.setText("Result: " + self.prediction3)
        return
    def makePerturbation(self):

        text = self.ui.plainTextEdit_2.toPlainText()
        # print(text)
        self.perturb_text = self.perturbation(text,1,90,10)
        # for char in "AEIOUaeiou":
        #     text = re.sub(char,random.choice(non_ascii_char[char]),text)
        self.ui.plainTextEdit_3.setPlainText(self.perturb_text)
        return
    def perturbation(self,text,min_freq,prob_vowel,prob_ascii):

        """ for comparation"""
        txt = self.preprocess.clean_txt(text)
        #   print("text_clean: ",txt)
        """ data which will be changed"""
        text_list = text.split()
        new_word = [word for word in txt.split()]

        # print("new_word", new_word)
        # print("new_word_len", len(new_word))
        #   print(new_word)
        word_found = []
        for word in new_word:
            if word in self.sig_word:
                word_found.append(word)
        # print("word_signi_found", word_found)
        word_freq_found = []
        num_del = int(len(new_word)*0.1)
        for i in range(num_del):
            if len(new_word) > 0:
                max_fq_word = max(set(new_word), key = new_word.count)
                new_word = [word for word in new_word if max_fq_word != word]
                word_freq_found.append(max_fq_word)
        print(word_freq_found)
        word_found_idx = []
        freq_word_idx = []
        #   print("word_found:",word_found_idx)
        for idx,word in enumerate(text.lower().split()):
            if self.preprocess.clean_txt(word) in word_found:
                word_found_idx.append(idx)
            if self.preprocess.clean_txt(word) in word_freq_found:
                freq_word_idx.append(idx)

        # print(freq_word_idx)

        """make perturbation"""
        for idx,word in enumerate(text_list):
            # print(idx,word)
        #     print("before:",text_list[idx])
        """ Swap character within the same word"""
            temp = list(word)
            if idx in word_found_idx:
                # print("word found", word)
                ra,rb = random.randrange(0,len(temp),1),random.randrange(0,len(temp),1)
                temp[ra], temp[rb] = temp[rb], temp[ra]
                text_list[idx] =  "".join(temp)
                # print("swaped",text_list[idx])
            else:
                if random.randrange(0,100,1) < 30:
                    ra,rb = random.randrange(0,len(temp),1),random.randrange(0,len(temp),1)
                    temp[ra], temp[rb] = temp[rb], temp[ra]
                    text_list[idx] =  "".join(temp)
            """ Character to graphically similar one"""
            for char in "AEIOUaeiou":
                if random.randrange(0,100,1) < prob_vowel:
                    rand_char = random.choice(self.non_ascii_char[char])
                    text_list[idx] = re.sub(char,rand_char,text_list[idx])
            for char in list(string.ascii_letters):
                if random.randrange(0,100,1) < prob_ascii:
                    if len(self.non_ascii_char[char])> 0:
                        rand_char = random.choice(self.non_ascii_char[char])
                        text_list[idx] = re.sub(char,rand_char,text_list[idx])
            # print(" ".join(text_list))

        freq_word_idx.sort(reverse = True)
        if len(freq_word_idx) < int(len(text_list)/3):
            for idx in freq_word_idx:
                del text_list[idx]

        return " ".join(text_list)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
