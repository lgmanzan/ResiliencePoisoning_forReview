## Importing
import sys
import csv
import os
import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import matthews_corrcoef

from google.colab import drive
drive.mount('/content/drive')


max_rounds = 5 #Choosen number 5 as an example
valuesHLayers = [5,50] #Choosen numbers  5,50 as an example
numhiddenLayer=[1,2] #Choosen numbers  1,2 as an example




## Reading input file
dfTrain = pd.read_csv('LOCATION TRAING FILE')



## Reading input file
dfTest = pd.read_csv('LOCATION TEST FILE')

## Converting strings to numbers by label encoding due to having ordinal strings
le = preprocessing.LabelEncoder()
dfTrain['state'] = le.fit_transform(dfTrain['state']) #now good 0 and bad 1


dfTest['state'] = le.fit_transform(dfTest['state']) #now good 0 and bad 1



with open('RESULTS FILE', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['HLnum','valueHL','mean_precision_score','mean_recall_score','mean_f1_score','mean_accuracy_score','TN','TP','FN','FP','matthews_corrcoef']) ## writing header

    for HLnum in numhiddenLayer:
        for valuesHL in valuesHLayers:
          # print('valuesHLayers:', valuesHLayers)
            n_rounds = 1
            precision_score_values = []
            recall_score_values = []
            f1_score_values = []
            accuracy_score_values = []
            matthewscoorf=[]
            tpL=[]
            tnL=[]
            fpL=[]
            fnL=[]
            while n_rounds <= max_rounds:
                varSizeIni=1
                varSizeFin=10 # Depends on the type of file which is processing, it should be chosen accordingly -- chosen 10 as an example
                varchar=varSizeFin-varSizeIni

                X_train = dfTrain.iloc[:, varSizeIni:varSizeFin] 
                y_train = dfTrain.loc[:,'state']

                X_test = dfTest.iloc[:, varSizeIni:varSizeFin]
                y_test = dfTest.loc[:,'state']


                under_sampler = RandomUnderSampler()
                X_resOrdered, y_resOrdered = under_sampler.fit_resample(X_train, y_train)

                dfOrdered = pd.concat([X_resOrdered,y_resOrdered], axis="columns")

                dfDisordered=dfOrdered.sample(frac = 1)
                characteristics=varchar 
                X_res = dfDisordered.iloc[:, 0:characteristics]
                y_res = dfDisordered.loc[:,'state']

                scaler = MinMaxScaler() 
                X_res = scaler.fit_transform(X_res)
                X_test = scaler.fit_transform(X_test)

                if HLnum==1:
                    classifier = MLPClassifier(hidden_layer_sizes=(valuesHL,), max_iter=1000,activation = 'tanh',solver='lbfgs',random_state=1)
                if HLnum==2:
                    classifier = MLPClassifier(hidden_layer_sizes=(valuesHL,valuesHL,), max_iter=1000,activation = 'tanh',solver='lbfgs',random_state=1)

                classifier.fit(X_res, y_res)

                ## Predictng the test set results
                y_pred = classifier.predict(X_test)

                ## Evaluating results
                precision_score_values.append(precision_score(y_test, y_pred))

                recall_score_values.append(recall_score(y_test, y_pred))

                f1_score_values.append(f1_score(y_test, y_pred))

                accuracy_score_values.append(accuracy_score(y_test, y_pred))
                
                tn, fp, fn, tp =confusion_matrix(y_test, y_pred).ravel()
                tnL.append(tn)
                tpL.append(tp)
                fnL.append(fn)
                fpL.append(fp)
                matthewscoorf.append(matthews_corrcoef(y_test, y_pred))

                n_rounds = n_rounds + 1

            writer.writerow([HLnum,valuesHL,round(np.mean(precision_score_values),2),round(np.mean(recall_score_values),2),round(np.mean(f1_score_values),2),round(np.mean(accuracy_score_values),2),round(np.mean(tnL),2),round(np.mean(tpL),2),round(np.mean(fnL),2),round(np.mean(fpL),2),round(np.mean(matthewscoorf),2)])
