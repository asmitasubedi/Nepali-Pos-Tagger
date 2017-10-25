import os
import ExtractFeatures
import xml.etree.ElementTree as ET
# path = 'H:\\FYP\\nepali pos\\nnc_updated_ah\\nnc_updated_ah\\cs\\a17.xml'
# filelist = os.listdir(path)
X, y, X_test, y_test, test_sen = [], [], [], [], []
temp = 0
path = 'H:\\FYP\\nepali pos\\nnc_updated_ah\\nnc_updated_ah\\cs\\a17.xml'
# filelist = os.listdir(path)
# for file in filelist:
#     filepath = os.path.join(path, file)
#     print(filepath)

tree = ET.parse(path)
root = tree.getroot()
single_sentence = []

for data in root.findall('text'):
            for value in data:
                # print(value.tag)
                if (value.tag == 'group'):
                    # for group in value.findall('group'):
                    for body in value.findall('body'):
                        for div in body.findall('div'):
                            for subdiv in div:
                                # print(subdiv.tag)
                                if (subdiv.tag == "head"):

                                    for sentence in subdiv.findall('s'):
                                        print(sentence.attrib)
                                        single_sentence = []
                                        for s in sentence:
                                            # print(s.attrib)
                                            if (s.tag == "foreign"):
                                                for words in s.findall('w'):
                                                    print("%s/%s" % (words.text, words.attrib['ctag']), '', end=''),
                                            # print("\n")
                                            if (s.tag == "w"):
                                                # print("%s %s" % (s.text, s.attrib['ctag']), '', end=''),
                                                single_sentence.append(s.text)
                                                single_sentence.append(s.attrib['ctag'])
                                                test_sen.append(s.text)
                                                y_test.append(s.attrib['ctag'])
                                        print(single_sentence)

                                        for x in range(0, len(single_sentence), 2):
                                            # print(get_features(single_sentence,x))
                                            X_test.append(ExtractFeatures.get_testfeatures(single_sentence, x))
                                #         # print('\n')
                                # print(len(single_sentence))
                                if (subdiv.tag == "p"):
                                    for sentence in subdiv.findall('s'):
                                        # print(sentence.attrib)
                                        single_sentence = []
                                        for s in sentence:
                                            if (s.tag == "foreign"):
                                                for words in s.findall('w'):
                                                  print("%s/%s" % (words.text, words.attrib['ctag']), '', end=''),
                                            # print("\n")
                                            if (s.tag == "w"):
                                                temp = temp+1
                                                # print("%s/%s" % (s.text, s.attrib['ctag']), '', end=''),
                                                single_sentence.append(s.text)
                                                single_sentence.append(s.attrib['ctag'])
                                                y.append(s.attrib['ctag'])

                                        for x in range(0, len(single_sentence), 2):
                                            X.append(ExtractFeatures.get_testfeatures(single_sentence, x))
                                            # temp = temp + 1

    # print(temp)
print(len(X), len(X_test))
print(len(y), len(y_test))

from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

clf = Pipeline([
            ('vectorizer', DictVectorizer(sparse=False)),
            ('classifier', LinearSVC())
        ])
clf.fit(X[:50000],y[:50000])  # Use only the first 10K samples if you're running it multiple times. It takes a fair bit :)

y_predict = (clf.predict(X_test))
print(test_sen)
print(y_predict)
accuracy = ((clf.score(X_test, y_test)) * 100)
print("Accuracy:", accuracy)

for x in range(0, len(test_sen)):
     print("%s/%s" % (test_sen[x], y_predict[x]),'', end='')

import pickle
pickle.dump(clf, open("RESULT.pickle", "wb"))

