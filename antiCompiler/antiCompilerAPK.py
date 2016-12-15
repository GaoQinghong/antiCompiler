#coding:utf-8
from androguard.core.bytecodes import apk
from  androguard.core.bytecodes import dvm
from androguard import session
import pandas as pd
import numpy as np
import csv
import os
import string
#
# filepath = '/Users/gaoqinghong/Downloads/homework/MachineLearning/apk'
# #resultpath='/Users/gaoqinghong/Downloads/homework/MachineLearning'
# #filelist = os.listdir(filepath)
#
#
# #soft="/Users/chengangbao/apks/"
#
# filepathlist = []
# apkfilename =[]
#
# for (dirpath, dirnames, filenames) in os.walk(filepath):
#     for filename in filenames:
#         apkfilename.append(filename)
#         apkpath=os.path.join(dirpath, filename)
#         filepathlist.append(apkpath)
#
# del apkfilename[0]
# del filepathlist[0]
# print filepathlist[0]
#
# permissions = []            # 获取所有apk文件的权限
# filename = []
# writer = csv.writer(open('/Users/gaoqinghong/Desktop/permission.csv','ab+'),delimiter='|',
#                             quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# j = 0
# print filepathlist[0]
# print len(filepathlist)
# print len(apkfilename)
#
# #反编译，获取每个apk的权限，写入permission.csv文件
# for i in range(len(filepathlist)):
#     try:
#         apkdoc = filepathlist[i]
#         s = session.Session()
#         with open(apkdoc, "r") as fd:
#             s.add(apkdoc, fd.read())
#         a, d, dx = s.get_objects_apk(apkdoc)
#         d = dvm.DalvikVMFormat(a.get_dex())
#     except Exception,ex:
#         continue
#     except UnicodeEncodeError,ex:
#         continue
#     except IndexError,e:
#         continue
#     print j, '(get) : ', a.get_permissions()  #打印输出获取到的权限
#     if(i<1000):
#         apktype = ['0']     #bad
#     else:
#         apktype = ['1']     #good
#     permissions.append(a.get_permissions())
#     writer.writerow([apkfilename[i]]+apktype+permissions[j])
#     j += 1


if __name__=='__main__':
    dictionary = {}
    with open('/Users/gaoqinghong/Desktop/permission.csv','r') as f:
        for line in f:
            string = line.split('|')
            dictionary[string[0]] = string[1:]
    features = set()
    for i in iter(dictionary):
        features = features.union(set(dictionary[i][1:]))
    print len(features)
    features.add('label')
    df = pd.DataFrame(data=np.zeros((len(dictionary.keys()),len(features)),dtype=int),index=dictionary.keys(),columns=features)
    for key in iter(dictionary):
        df.loc[key,dictionary[key][1:]] = 1
        df.loc[key,'lable'] = dictionary[key][0]
    df.to_csv('./features.csv')



