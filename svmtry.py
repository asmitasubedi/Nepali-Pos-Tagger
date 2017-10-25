from sklearn import svm
from sklearn import tree
# X = [[0, 0], [1, 1]]
# y = [0, 1]
# clf = svm.SVC()
# clf.fit(X, y)
# predicted = clf.predict([[2., 2.]])
# print(predicted)
# # get support vectors
# print(clf.support_vectors_)
# # get indices of support vectors
# print(clf.support_)
# # get number of support vectors for each class
# print(clf.n_support_)

# from sklearn import datasets
# from sklearn.multiclass import OneVsRestClassifier
# from sklearn.svm import LinearSVC
# iris = datasets.load_iris()
# X, y = iris.data, iris.target
# print(len(y))
# OneVsRestClassifier(LinearSVC(random_state=0)).fit(X, y).predict(X)

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import svm, datasets
# # import some data to play with
# iris = datasets.load_iris()
# X = iris.data[:, :2] # we only take the first two features. We could
#  # avoid this ugly slicing by using a two-dim dataset
# y = iris.target
# # we create an instance of SVM and fit out data. We do not scale our
# # data since we want to plot the support vectors
# C = 1.0 # SVM regularization parameter
# svc = svm.SVC(kernel='linear', C=1,gamma=0).fit(X, y)


from sklearn.feature_extraction import DictVectorizer
pos_window = [
    {
        'word-2': 'the',
        'pos-2': 'DT',
        'word-1': 'cat',
        'pos-1': 'NN',
        'word+1': 'on',
        'pos+1': 'PP',
    },
{
        'word-2': 'cat',
        'pos-2': 'DT',
        'word-1': 'fox',
        'pos-1': 'NN',
        'word+1': 'love',
        'pos+1': 'PP',
    },
    # in a real application one would extract many such dictionaries
]
pos_class = [{'pos':'NN'}, {'pos':'PQ'}]

print(pos_window,pos_class)
vec = DictVectorizer()
# feature_vectorized = vec.fit_transform(pos_window)
# pos_vectorized = vec.fit_transform(pos_class)
# print(feature_vectorized,pos_vectorized)
X = vec.fit_transform(pos_window).toarray()
y = vec.fit_transform(pos_class).toarray()
# y = (pos_vectorized.toarray())
# print(vec.get_feature_names())

# y =
C = 1.0  # SVM regularization parameter

# SVC with linear kernel
# svc = svm.SVC(kernel='linear', C=C).fit(X, y)
import collections
import nltk


def assess(text, predictions_actual):
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)
    for i, (prediction, actual) in enumerate(predictions_actual):
        refsets[actual].add(i)
        testsets[prediction].add(i)
    speaker_precision = nltk.metrics.precision(refsets[True], testsets[True])
    speaker_recall = nltk.metrics.recall(refsets[True], testsets[True])
    non_speaker_precision = nltk.metrics.precision(refsets[False], testsets[False])
    non_speaker_recall = nltk.metrics.recall(refsets[False], testsets[False])
    return [text, speaker_precision, speaker_recall, non_speaker_precision, non_speaker_recall]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
predictions = clf.predict(X)
assessment = assess("Decision Tree", zip(predictions, X))
print(assessment)
