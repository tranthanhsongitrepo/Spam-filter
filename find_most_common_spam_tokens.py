import csv

import nltk
import Pair as ult

common_words = []

email_fileName = 'emails.csv'
output = 'common_spam_tokens.txt'

# Open email file
with open(email_fileName) as f:
    reader = csv.reader(f, delimiter=',')
    for mail in reader:
        # Tokenize mail's subject
        tokens = nltk.wordpunct_tokenize(mail[0])[2:]

        for word in tokens:
            # Find word's index in common_words
            index = ult.find(common_words, word)

            # If common_words doesn't contains word and it's a spam mail
            if index == -1 and mail[1] == 'Spam':
                common_words.append(ult.Pair(word))

            # Else if mail is a spam mail, increase frequency counter, if not, decrease frequency counter
            else:
                common_words[index].addFreq(1 if mail[1] == 'Spam' else -1)

# Sort list in descending frequency order
common_words.sort(reverse=True)

# Write 2500 first items to output file
with open(output, 'w') as f:
    for i in range(0, 2500):
        f.write(common_words[i].getWord() + '\n')
