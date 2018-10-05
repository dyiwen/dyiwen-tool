#!/usr/bin/env python
# encoding: utf-8

import DAL,json,re,os
import pydicom
import traceback

def select_guz_info():
    try:
        msl = DAL.Mysql("host", "port", "user", "pwd", "databases")

        '''sql = "select distinct patientid,modality,body,exam_item,exam_date,impression \
        from VIEW_NAME \
        where impression like '%骨折%' and modality like '%CT%' and body like '%胸%' and (exam_date between '2018-07-18' and '2018-07-22')" '''
        
        sql = "select distinct patientid,SUID\
        from TX_PATIENT_BASIC_INFO \
        where impression like '%骨折%' and modality like '%CT%' and body like '%胸%' \
        and (exam_date between '2018-06-20' and '2018-07-23') and impression not like '%未见明显错位性骨折%' \
        and impression not like '%未见明显骨折%'and impression not like '%未见明确骨折%' and impression not like '%未见明确挫伤及骨折征象%'"

        rowcount,result = msl.execute(sql)
        msl.close()
    except:
        print("sql 失败!")
    print result 
    return result


#-----------------------------------------------------------------------------------

def get_pull_id():
    root = '/media/.../Data/DICOMS/GUZE/CT'
    #root = '/media/.../Data/DICOMS/CT'
    root_patient_list = os.listdir(root)
    print root_patient_list
    print 'The total num of patientid in root is :',len(root_patient_list)
    return root_patient_list

def root_id():
    a = select_guz_info()
    patientid = [patient[0] for patient in a]
    print len(patientid)
    b = get_pull_id()
    root_id_list = [v for v in b if v in patientid]
    print root_id_list
    print 'Totally find out :',len(root_id_list)
    return root_id_list



def check_lock():
    a = select_guz_info()                        #sql_list
    patientid = [patient[0] for patient in a]
    print len(patientid)
    b = get_pull_id()                             #root_list
    lock_list = [v for v in patientid if v not in b]
    print lock_list
    print len(lock_list)


def check_file_num():
    a = get_pull_id()     #pull_list
    #a = root_id()          #root_list
    n = 0
    path_list = []
    for i in a:
        print i,'#--------------------------------------------------------------------------'
        root = "/media/.../Data/DICOMS/GUZE/CT/"+'{}'.format(i)
        #root = "/media/.../Data/DICOMS/CT/"+'{}'.format(i)
        #print 'patient:',os.listdir(root)
        for roots,dirs,files in os.walk(root):
            if len(files) > 59:
                print len(files)
                print roots,'\n'
                path_list.append(roots)

        n += 1

    print path_list
    print 'The full quality of num is :',n
    return path_list

def check_dicom_tag(): 
    a = check_file_num()
    SIMEN = ['B60f','B70s','B90s','B30f','B75s','B31s','B31f','B80f',['180s','3'],['150f','3'],['I70f','3'],['Br40d','3']]
    Phli = ['YB','YA','L','YD','E']
    GUZE_data = []
    for i in a :
        try:
            xx = 'T/(.*?)/'
            rex = re.compile(xx)
            result_ = rex.search(i).group()
            xxx = r'\d{8,13}'
            rexx = re.compile(xxx)
            result_2 = rexx.search(result_).group()
            print result_2,'************************'


            dicom = os.listdir(i)[0]
            gdcm_path = os.path.join(i,dicom)
            #print gdcm_path
            #-------------------------------------------------------------------------------------------------
            ds = pydicom.read_file(gdcm_path)
            conk = ds.ConvolutionKernel
            manu = ds.Manufacturer
            if ds.Manufacturer == 'SIEMENS' and ds.ConvolutionKernel in SIMEN:
                print '-------------------SIEMENS-----------------------------------------'
                print 'ConvolutionKernel is :',conk
                print 'Manufacturer is :',manu
                print 'ProtocolName is :',ds.ProtocolName
                GUZE_data.append([manu,conk,i,result_2])
            elif ds.Manufacturer == 'Philips' and ds.ConvolutionKernel in Phli:
                print '-------------------Philips------------------------------------------'
                conk = ds.ConvolutionKernel
                manu = ds.Manufacturer
                print 'ConvolutionKernel is :',conk
                print 'Manufacturer is :',manu
                print 'ProtocolName is :',ds.ProtocolName
                GUZE_data.append([manu,conk,i,result_2])
            elif ds.Manufacturer not in ['SIEMENS','Philips']:
                print manu
            else:
                # print '##################################################'
                print 'NOT FULL'
                # print 'ConvolutionKernel is :',ds.ConvolutionKernel
                # print 'Manufacturer is :',ds.Manufacturer
                # print '##################################################'
                #---------------------------------------------------------------------------------------------------
        except Exception as e:
            print result_2,traceback.print_exc()
            continue

    print GUZE_data
    print 'go find :',len(GUZE_data)
    return GUZE_data



def mv_data():
    target_data = check_dicom_tag()

    for data in target_data:
        from_path = data[2]+'/'
        to_path = "/media/.../'Seagate Expansion Drive'/c_move/guzhe/"+data[0]+'/'+data[1]+'/'+data[3]
        check_path = "/media/.../Seagate Expansion Drive/c_move/guzhe/"+data[0]+'/'+data[1]+'/'+data[3]
        if os.path.exists(check_path):
            print 'True'
        else:
            print 'False'
            cmd = 'mkdir -p' + ' '+to_path
            #print cmd
            os.system(cmd)
        cmd2 = "cp -r {} {}".format(from_path.replace('Seagate Expansion Drive',"'Seagate Expansion Drive'"),to_path)
        a = os.popen(cmd2).read()
        print 'done 1'










if __name__ == '__main__':
	#get_pull_id()
	#check_file_num()
	check_dicom_tag()
	#check_lock()
	#mv_data()
    #root_id()
