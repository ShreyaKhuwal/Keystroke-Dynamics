# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:01:28 2020

@author: Shreya Khuwal
"""
import pandas as pd
from sklearn.externals import joblib


#Feature Extraction part
#Output - array of input (n,N_features)
X_test=pd.read_csv('testuser2.csv',header=0)  #test file

X_test=X_test[['ll','rr','lR','Lr','rL','Rl','lL','rR','lr','rl','Enter','Space','l','L','r','R',
                                     'Backspace','cpm']]
X_test=X_test.values
GMM_classifier=joblib.load('GMMclassifier.pkl')
y_test=GMM_classifier.predict(X_test)

Person={1:'Shreya',2:'Neha',3:'Divi',4:'Jhala',5:'Purva'}

y_test_length=len(y_test)
y_=y_test.tolist()
mode=max(set(y_), key=y_.count)
frequency=y_.count(mode)
accuracy=float(frequency)/len(y_)*100
if  accuracy > 60:
    print ("The Person identified typing is ", Person[mode],"with",round(accuracy,2),"% accuracy")
else:
    print ("Impostor!")
