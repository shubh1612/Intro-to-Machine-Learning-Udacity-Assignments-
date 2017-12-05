#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy as np
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
features_train = features_train[:len(features_train)]
labels_train = labels_train[:len(labels_train)]
from sklearn.svm import SVC
clf = SVC(C = 10000.0, kernel = "rbf")
clf.fit(features_train, labels_train)
y_pred = clf.predict(features_test)
print np.count_nonzero(y_pred==1)
print accuracy_score(labels_test, y_pred)
#########################################################


