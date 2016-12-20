#coding:utf-8
from sklearn.svm import SVC
from sklearn import svm
from sklearn.model_selection import cross_val_score
from  sklearn.model_selection import cross_val_predict
from sklearn import metrics
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from  sklearn.preprocessing import normalize
import csv



if __name__ == '__main__':
    # 降低permission的维度
    df = pd.read_csv('/Users/gaoqinghong/Downloads/features.csv',sep=',')
    sum = []
    for colnumber in range(1,len(df.columns)-1):
        sumbadnum = 0
        sumgoodnum = 0
        for rownumber in range(len(df.index)):
            if(df.iloc[rownumber,-1]=='0'):
                sumbadnum += int(df.iloc[rownumber, colnumber])
            else:sumgoodnum += int(df.iloc[rownumber,colnumber])
        if(abs(sumbadnum-sumgoodnum)<50):
            sum.append(df.columns[colnumber])
        print 'get:  ', colnumber
    for colname in sum:
        del df[colname]
    print 'dimension: ',len(df.columns)
    df.to_csv('/Users/gaoqinghong/Desktop/reduceDim.csv')


    #线性SVM模型训练测试
    # df = pd.read_csv('/Users/gaoqinghong/Desktop/reduceDim.csv',sep=',')
    # X = np.array(df.iloc[:,2:-2])
    # Y = np.array(df.iloc[:,-1])
    # poly = PolynomialFeatures(degree=2,interaction_only=True)
    # X = poly.fit_transform(X)
    # # sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
    # # X = sel.fit_transform(X)
    # X = normalize(X)
    # clf = svm.LinearSVC()
    # predicted = cross_val_predict(clf,X,Y,cv=15)
    # print metrics.accuracy_score(Y,predicted)






