#!/usr/bin/env python
# encoding: utf-8

import DAL,json,re,os
import pydicom

def show_chinese(data):
    show_china = json.dumps(data,encoding = 'UTF-8',ensure_ascii = False)
    return show_china

def select_guz_info():
    try:
        msl = DAL.Mysql("HOST", "PORT", "USER", "PWD", "DATABASE")

        '''sql = "select distinct patientid,modality,body,exam_item,exam_date,impression \
        from VIEW_NAME \
        where impression like '%骨折%' and modality like '%CT%' and body like '%胸%' and (exam_date between '2018-07-18' and '2018-07-22')" '''
        
        sql = "select distinct patientid,SUID\
        from TX_PATIENT_BASIC_INFO \
        where impression like '%骨折%' and modality like '%CT%' and body like '%胸%' \
        and (exam_date between '2018-05-15' and '2018-05-19') and impression not like '%未见明显错位性骨折%' \
        and impression not like '%未见明显骨折%'and impression not like '%未见明确骨折%' and impression not like '%未见明确挫伤及骨折征象%'"

        rowcount,result = msl.execute(sql)
        msl.close()
    except:
        print("sql 失败!")
    print result 
    return result
#-------------------------------------------------Local_Service--------------------------------------------------------------------
def check_key_word():
    a = select_guz_info()
    patient_id_list = [patient_id[0] for patient_id in a ]
    #print patient_id_list
    print 'Total num of GUZE is :',len(a)
    return patient_id_list

def get_pull_id():
    root = '/media/.../Data/DICOMS/CT'
    cmd = 'cd /media/.../Data/DICOMS/CT && (ls -al)'
    root_patient_list = os.listdir(root)
    print root_patient_list
    print 'The total num of patientid in root is :',len(root_patient_list)
    return root_patient_list

def target_id():
    sql_id = check_key_word()
    root_id = get_pull_id()
    target_id = [i for i in sql_id if i in root_id]
    print 'There has',len(target_id)
    lock_id = [v for v in sql_id if v not in root_id ]
    print 'The Not have :',len(lock_id)
    return target_id

def check_file_num():
    a = target_id()
    n = 0
    path_list = []
    for i in a:
        print i,'#--------------------------------------------------------------------------'
        root = '/media/.../Data/DICOMS/CT'+'/{}'.format(i)
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
        dicom = os.listdir(i)[0]
        gdcm_path = os.path.join(i,dicom)
        # cmd = "gdcmdump {} | grep -E 'Convolution Kernel|Manufacturer'".format(gdcm_path)
        # find_result = os.popen(cmd).read()
        #['Philips', 'SIEMENS']
        ds = pydicom.read_file(gdcm_path)
        if ds.Manufacturer == 'SIEMENS' and ds.ConvolutionKernel in SIMEN:
            print '-------------------SIEMENS-----------------------------------------'
            print 'ConvolutionKernel is :',ds.ConvolutionKernel
            print 'Manufacturer is :',ds.Manufacturer
            print 'ProtocolName is :',ds.ProtocolName
            GUZE_data.append(i)
        elif ds.Manufacturer == 'Philips' and ds.ConvolutionKernel in Phli:
            print '-------------------Philips------------------------------------------'
            print 'ConvolutionKernel is :',ds.ConvolutionKernel
            print 'Manufacturer is :',ds.Manufacturer
            print 'ProtocolName is :',ds.ProtocolName
            GUZE_data.append(i)


    print 'The totally num of find is :',len(GUZE_data)
    print GUZE_data
    return GUZE_data

def cp_files():
    path_list = check_dicom_tag()
    for i in path_list:
        print '######################################################3'
        print i
        xx = "/CT/(.*?)/"
        rex = re.compile(xx)
        patient_id = rex.search(i).group()
        xxx = '\d{8,13}'
        rexx = re.compile(xxx)
        id_ = rexx.search(patient_id).group()
        print id_
        from_ = i+'/'
        to_ = "./{}".format(id_)
        cmd = "cd /media/.../'Seagate Expansion Drive'/GUZE && cp -r {} {}".format(from_,to_)
        #print cmd
        os.system(cmd)
#---------------------------------------------------------------------------------------------------------------------
def get_list_move():
    a = select_guz_info()
    print a
    n = 0 
    for p_id,suid in a:
        #print p_id,suid
        cmd = "/usr/local/bin/movescu --study -aet xxxx -aec xxxx -aem xxxx -v -d  host   4100 -k  08,52=STUDY -k \
        StudyInstanceUID={} --output-directory /media/.../'Seagate Expansion Drive'/c_move/".format(suid)
        result = os.popen(cmd).read()
        print result
        n += 1
    print 'The total num of pilling is :',n







if __name__ == '__main__':
	#select_guz_info()
    #check_key_word()
    #get_pull_id()
    #target_id()
    #check_file_num()
    #check_dicom_tag()
    #cp_files()

    get_list_move()




    #/usr/local/bin/movescu --study -aet TXPACS -aec GEPACS -aem TXPACS -v -d  10.3.1.189   4100 -k  08,52=STUDY -k StudyInstanceUID={accessionno}
