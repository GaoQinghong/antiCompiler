#coding:utf-8
from androguard.core.bytecodes import apk
import os

filepath = '/Users/gaoqinghong/Downloads/homework/MachineLearning/apk'
#resultpath='/Users/gaoqinghong/Downloads/homework/MachineLearning'
filelist = os.listdir(filepath)

listAllApkFile = []      #存储所有apk文件名
listfilepath = []         #存储bad，good1，good2文件夹的路径
i = 0
for list in filelist:    #读取所有apk文件名，存储到list内
    if(i == 0):
        i += 1
        continue
    filepathnow = filepath+'/'+list
    listfilepath.append(filepathnow)
    listAllApkFile = listAllApkFile+os.listdir(filepathnow)
    #print len(listAllApkFile)

filepathlist = []
for list in range(1000):
    filepathlist.append(listfilepath[0]+'/'+listAllApkFile[list])

for list in range(499):
    filepathlist.append(listfilepath[1]+'/'+listAllApkFile[1000+list])

for list in range(500):
    filepathlist.append(listfilepath[2] + listAllApkFile[1499+list])

print len(filepathlist)


apkclass = []            # 为每个apk文件创建一个对象
for i in range(len(filepathlist)):
    apkclass.append(apk.APK(filepathlist[i], raw=False))

permissions = []
for list in range(len(apkclass)):
   permissions[list] = apkclass[list]




