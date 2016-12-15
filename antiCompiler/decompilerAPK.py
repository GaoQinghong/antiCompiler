#coding:utf-8
#!/usr/bin/env python

import sys, hashlib

from androguard.core.analysis import analysis
from androguard.session import Session
from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm
import re
import os

def get_apis(app, app_dex, app_x):  # 取得apk的API，返回api列表
    methods = set()
    cs = [cc.get_name() for cc in app_dex.get_classes()]
    for method in app_dex.get_methods():
        g = app_x.get_method(method)
        if method.get_code() == None:
            continue
        for i in g.get_basic_blocks().get():
            for ins in i.get_instructions():
                # This is a string that contains methods, variables, or anything else.
                output = ins.get_output()
                match = re.search(r'(L[^;]*;)->[^\(]*\([^\)]*\).*', output)
                if match and match.group(1) not in cs:
                    methods.add(match.group())
    methods = list(methods)
    methods.sort()
    return methods




soft = '/Users/gaoqinghong/Downloads/homework/MachineLearning/apk'
outputPath='/Users/gaoqinghong/Downloads/homework/MachineLearning'


# TEST = "/Users/chengangbao/apks/air.MagicMirror.apk"
apklist=[]

for (dirpath, dirnames, filenames) in os.walk(soft):
    # for dirname in dirnames:
    #     print('dirname = ' + dirname)
    for filename in filenames:
        apkpath=os.path.join(dirpath, filename)
        apklist.append(apkpath)
del apklist[0]
# print len(apklist)
# for i in range(998,1003):
#     print apklist[i]
# cmd1="sh /Users/chengangbao/apkpackage/dex2jar-2.0/d2j-dex2jar.sh {0}".format(apklist[10])
# os.system(cmd1)

# for i in range(len(apklist)):
for i in range(990,1010):
    apkdoc=apklist[i]
    # s = Session()
    # with open(apkdoc, "r") as fd:
    #     s.add(apkdoc, fd.read())
    # a, d, dx = s.get_objects_apk(apkdoc)
    a=apk.APK(apkdoc)
    d = dvm.DalvikVMFormat(a.get_dex())
    aly = analysis.newVMAnalysis(d)
    print get_apis(a, d, aly)
    #print a.get_permissions()
    # print i
    # print 'min_sdk_version: ',a.get_min_sdk_version()
    # print 'androidversion_code: ',a.get_androidversion_code()
    # print 'providers: ',a.get_providers()
    # print 'receivers: ',a.get_receivers()
    # print 'services: ',a.get_services()
    # print 'methods(1): ',d.get_methods()[1]
    # print 'methods len: ',len(d.get_methods())
    # print 'fields len: ',len(d.get_fields())
    # print 'fields(0): ',d.get_fields()[0]
    # print 'classes(0): ',d.get_classes()[0]
    # print 'classes len: ',len(d.get_classes())
    # print 'string data item len: ',len(d.get_string_data_item())
    # print 'classes name: ',len(d.get_classes_names())
    # print '\n'


