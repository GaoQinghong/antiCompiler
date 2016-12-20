#coding:utf-8
from androguard.core.bytecodes import apk
from  androguard.core.bytecodes import dvm
from androguard import session
from sklearn.svm import SVC
from sklearn import svm
from sklearn.model_selection import cross_val_score
from  sklearn.naive_bayes import  GaussianNB
from  sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import numpy as np
import pandas as pd


import csv
import os
import string
#
filepath = '/Users/gaoqinghong/Downloads/homework/MachineLearning/test_apk'
#resultpath='/Users/gaoqinghong/Downloads/homework/MachineLearning'
#filelist = os.listdir(filepath)


#
filepathlist = []
apkfilename =[]

for (dirpath, dirnames, filenames) in os.walk(filepath):
    for filename in filenames:
        apkfilename.append(filename)
        apkpath=os.path.join(dirpath, filename)
        filepathlist.append(apkpath)
#print apkfilename[0]
del apkfilename[0]
del filepathlist[0]
print filepathlist[0]
#


#获取所有apk文件的权限
permissions = []
filename = []
writer = csv.writer(open('/Users/gaoqinghong/Desktop/permission.csv','ab+'),delimiter='|', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
j = 0
#反编译，获取每个apk的权限，写入permission.csv文件
for i in range(len(filepathlist)):
    try:
        apkdoc = filepathlist[i]
        s = session.Session()
        with open(apkdoc, "r") as fd:
            s.add(apkdoc, fd.read())
        a, d, dx = s.get_objects_apk(apkdoc)
        d = dvm.DalvikVMFormat(a.get_dex())
    except Exception,ex:
        continue
    except UnicodeEncodeError,ex:
        continue
    except IndexError,e:
        continue
    print j, '(get) : ', a.get_permissions()  #打印输出获取到的权限
    # if(i<1000):
    #     apktype = ['0']     #bad
    # else:
    #     apktype = ['1']     #good
    apktype = ['2']
    permissions.append(a.get_permissions())
    print [apkfilename[i]]+apktype+permissions[j]
    #writer.writerow([apkfilename[i]]+apktype+permissions[j])
    j += 1

# use SVM to predict
# if __name__=='__main__':
#     df = pd.read_csv('/Users/gaoqinghong/Downloads/homework/MachineLearning/features.csv',sep=',')
#     df_test = pd.read_csv('/Users/gaoqinghong/Desktop/test_features.csv',sep=',')
#     #clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
#     #Gnb = GaussianNB()
#     clf = svm.LinearSVC()
#     # print df.iloc[:1200,:-1]
#     # print '********************'
#     # print df.iloc[:1200,-1]
#     # print '###########'
#     # print '###############'
#     X = np.array(df.iloc[:,1:-2])
#     Y = np.array(df.iloc[:,-1])
#     X_test = np.array(df_test.iloc[:,1:-2])
#     clf.fit(X,Y)
#     print clf.predict(X_test)
#     #predicted1 = cross_val_predict(clf, X, Y, cv=10)
#     #print predicted1
#     print '***************'

    # predicted2 = cross_val_predict(Gnb, X, Y, cv=10)
    # print predicted2
    # print '***************'
    # print metrics.accuracy_score(Y, predicted2)
#
#
#     print '*********'
#     print 'same: ',metrics.accuracy_score(predicted1,predicted2)
#     print '**********'
#     print 'len2',len(predicted2)
#     print 'len1',len(predicted1)
#     listsame = []
#     listsame2 = []
#     for i in range(len(predicted1)):
#         listsame.append('2')
#         listsame2.append('2')
#
#     for i in range(len(predicted1)):
#         if(Y[i]!=predicted1[i]):
#             listsame[i] = predicted1[i]
#
#     for i in range(len(predicted1)):
#         if (Y[i] == predicted2[i]):
#             listsame2[i] = Y[i]
#
#
#     count1 = 0
#     for i in range(len(predicted1)):
#         if(listsame[i]!='2'):
#             count1 += 1
#     print 'count1: ',count1
#
#     count2 = 0
#     for i in range(len(predicted2)):
#         if (listsame2[i]=='2'):
#             count2 += 1
#     print 'count2 : ',count2
#
#     count = 0
#     for i in range(len(predicted1)):
#         if(listsame[i]!='2'):
#             if(listsame2[i]!='2'):
#                 count += 1
#     print 'count : ',count

    #scores1 = cross_val_score(clf,X,Y,cv=10)
    #print scores1
    #print 'accuracy:',scores1.mean()
    #print 'max: ',scores1.max()

    #scores2 = cross_val_score(Gnb, X, Y, cv=10)
    #print scores2
    #print 'accuracy:', scores2.mean()
    #print 'max: ', scores2.max()



    #X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
    #clf.fit(X_train,Y_train)
    #print Gnb.score(X_test,Y_test)
    # print metrics.accuracy_score(trueY,clf.predict(predictX))
    #


#获取反编译失败的文件名
# apkname = set()
# failed = []
# with open('/Users/gaoqinghong/Desktop/test_permission.csv', 'r') as f:
#     for line in f:
#         string = line.split('|')
#         apkname.add(string[0])
# #print apkname
#
# for i in range(len(apkfilename)):
#     if(apkfilename[i] not in apkname):
#         failed.append(apkfilename[i])
#
# failed_writer = csv.writer(open('/Users/gaoqinghong/Desktop/failed.csv','ab+'),delimiter=',')
# failed_writer.writerow(failed)