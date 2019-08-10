import csv
import nltk
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import Pair as ult

common_spam_word_fileName = 'common_spam_tokens.txt'
email_data_fileName = 'emails.csv'
my_spam_fileName = 'my_spam_mail.txt'

# Read common spam words
common_spam_words = open(common_spam_word_fileName, 'r').read().split('\n')

# Encode spam words
spam_word_label_encoder = LabelEncoder()
spam_word_label_encoder.fit(common_spam_words)


# Utility function to get spam data
def build_app(word_list):
    # Initiate all spam word freq as 0
    spam_word_freq = np.zeros(len(common_spam_words))

    for x in word_list:
        # If current word is a spam word, count it
        if x in common_spam_words:
            spam_word_freq[spam_word_label_encoder.transform([x])] += 1

    app = []
    tokens_length = len(word_list)

    # Append spam words frequency to app
    for i in spam_word_freq:
        app.append(0 if tokens_length == 0 else i / tokens_length)

    return app


def get_spam_data():
    X = []
    y = []
    with open(email_data_fileName, 'r') as f:
        email_read = csv.reader(f, delimiter=',')
        for line in email_read:
            # Tokenize mail
            tokens = nltk.wordpunct_tokenize(line[0])[2:]

            # Add data to X
            X.append(build_app(tokens))

            # Add test result to y_test
            y.append(1 if line[1] == 'Spam' else 0)

    return X, y


clf = GaussianNB()

X, y = get_spam_data()

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# show_confusion_matrix(y_test, y_pred)

print('Predicted score : ', accuracy_score([int(x) for x in y_test], y_pred))

word_freq = []
with open(my_spam_fileName) as f:
    spam_mail = f.read()

    words = nltk.wordpunct_tokenize(spam_mail)

    test = [build_app(words)]

    print('Spam' if clf.predict(test) == 1 else 'Not Spam')