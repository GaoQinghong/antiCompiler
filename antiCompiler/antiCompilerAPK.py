#coding:utf-8
from androguard.core.bytecodes import apk
import os

filepath = '/Users/gaoqinghong/Downloads/homework/MachineLearning/apk'
#resultpath='/Users/gaoqinghong/Downloads/homework/MachineLearning'
filelist = os.listdir(filepath)

listAllApkFile = []      #存储所有apk文件名
i = 0
for list in filelist:    #读取所有apk文件名，存储到list内
    if(i == 0):
        i += 1
        continue
    filepathnow = filepath+'/'+list
    listAllApkFile = listAllApkFile+os.listdir(filepathnow)


apkclass = []            # 为每个apk文件创建一个对象
for i in range(len(listAllApkFile)):
    apkclass[i] = apk.APK(filepath + "/" + "bad" + "/" + listAllApkFile[1], raw=False, mode='r', magic_file=None, zipmodule=1)

permission = apk.get_permissions()
for list in permission:
    print list




