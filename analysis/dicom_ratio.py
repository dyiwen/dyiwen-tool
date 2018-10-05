#! usr/bin/env python
# -*- coding:utf8 -*-
# encoding=utf-8
import os,time,sys,re,pydicom
import pprint

#roots = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data'

#roots = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data/two-dicom/0001614904'

#roots = '/media/dyiwen/KINGSTON/tuomin/jiangning/830974'

#头部
#roots = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data/two-dicom/0001650242'

#roots = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data/lots'
#roots = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data/single-dicom'
roots = '/media/.../Data/DICOMS/CT/N12275942'  #0001438340 #0001452575
def file_num(path):
    patient_data = []
    n = 0
    for root,dirs,files in os.walk(path):
        if len(files) < 20:
            continue
        rex = re.compile(r'\d{8,13}')
        a = rex.search(root).group()
        p_list = [a,root,len(files),files[0]]
        #print '--------------------------next-one---------------------------------------------'
        patient_data.append(p_list)
        n += 1
        if n == 50:
            break
    print patient_data
    print '共查到{}套数据'.format(len(patient_data))
    dicom_path_list = [os.path.join(patient[1],patient[3])for patient in patient_data]
    print dicom_path_list
    big_string = []
    for dicom_path in dicom_path_list:
        ds = pydicom.read_file(dicom_path)
        for line in str(ds).splitlines():
            big_string.append(line.strip())
    big_string.insert(0,len(patient_data))
    return big_string

def count_dicom(path):
    mylist = file_num(path)
    print '1111',mylist
    #mystring = ','.join(mylist)
    a = {}
    for i in mylist:
        if mylist.count(i)>1:
            a[i] = '{:.2%}'.format(float(mylist.count(i))/mylist[0])
            # a[i] = float(mylist.count(i))/16
    pprint.pprint(a)


def grep_search(path):
    patient_data = []
    for root,dirs,files in os.walk(path):
        if len(files) < 20:
            continue
        rex = re.compile(r'\d{8,13}')
        a = rex.search(root).group()
        p_list = [a,root,len(files),files[0]]
        #print '--------------------------next-one---------------------------------------------'
        patient_data.append(p_list)
    print patient_data
    print '共查到{}套数据'.format(len(patient_data))
    dicom_path_list = [os.path.join(patient[1],patient[3])for patient in patient_data]
    #print dicom_path_list
    print('---------------------------------------------------------------------------------------------')
    for dicom_path in dicom_path_list:
        print dicom_path
        cmd = "gdcmdump {} | grep -E 'Private | Protocol Name' | grep -v 'Private Creator'".format(dicom_path)
        result = os.popen(cmd).read()
        print(result)
        print('-----------------------------------------------------------------------------------')

count_dicom(roots)
#grep_search(roots)
