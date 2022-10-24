#impoer library
import numpy as np 
import pandas as pd 
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score

data = pd.read_csv("/content/spam.csv")
data = data.drop(['Unnamed: 2', 'Unnamed: 3'	, 'Unnamed: 4'], axis=1)
data['text'] = data['v2']
data['spam'] = data['v1']
data = data.drop(['v1', 'v2'], axis=1)

data.drop_duplicates(inplace = True)

nltk.download('stopwords')

def process_text(text):
  nopunc = [char for char in text if char not in string.punctuation]
  nopunc = "".join(nopunc)
  clean_word = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
  return clean_word
  
message_bow = CountVectorizer(analyzer = process_text).fit_transform(data['text'])

X_train, X_test, y_train, y_test = train_test_split(message_bow, data['spam'], test_size = 0.2, random_state=0)

classifier = MultinomialNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

def score(test,pred, size):
  count_value_count = (test == pred).sum()
  return (count_value_count / size) * 100
  
print(f"This model guessed {score(y_test, y_pred, y_test.shape[0])} % value correctly")
