#!usr/bin/env python
# -*-coding:utf-8-*-

import os,time,re,commands

#----------config_params----------------------------
channel = 'ct0'
cmd = 'docker ps -a | grep {}'.format(channel)
end_date = '2018-07-10'
search_date = 'Jul 10'
since_date = '"2018-07-10"'


def search_pid():

#--------------------------------------------
	result1 = os.popen(cmd).read()
	print result1
	#rex = re.compile(r'[\a-z0-9]{12}')
	rex = re.compile(r'\w{12}')
	PID = rex.search(result1).group()
	print PID
#---------------------------------------------

	cmd2 = 'docker logs {} --until {}'.format(PID,end_date)
	#result2 = os.popen(cmd2).read()
	#print result2
	result2 = commands.getoutput(cmd2)
	print result2
	#xx = r'\d{3,7}'
	xx = r'"patid": "\d{3,8}"'
	rex2 = re.compile(xx)
	patient_id_list = rex2.findall(result2)
	#print patient_id_list
	#print len(patient_id_list)

	search_list = []
	for patient_id in patient_id_list:
		#print patient_id
		if patient_id not in search_list:
			search_list.append(patient_id)
	#print search_list

	p_id_list = []
	for p_id in search_list:
		rex3 = re.compile(r'\d{3,8}')
		p_id = rex3.search(p_id).group()
		p_id_list.append(p_id)
	print p_id_list
	print 'The number of Ids those were searched is :',len(p_id_list)
	#for i in p_id_list:
		#if i in search_CT_number():
			#print 'The {} is : {}'.format(search_date,i)


def search_CT_number():
	cmd = 'cd /media/.../Data/DICOMS/CT && (ls -al | grep "{}")'.format(search_date)
	result = os.popen(cmd).read()
	#print result
	search_list = [i for i in result.splitlines()]
	#print search_list
	number_list = [patient_id[62:] for patient_id in search_list]
	print number_list[1:]
	return number_list[1:]

def serach_since():
	#--------------------------------------------
	result1 = os.popen(cmd).read()
	print result1
	#rex = re.compile(r'[\a-z0-9]{12}')
	rex = re.compile(r'\w{12}')
	PID = rex.search(result1).group()
	print PID
#---------------------------------------------
	cmd3 = 'docker logs -t --since={} {}'.format(since_date,PID)
	print cmd3

	result2 = commands.getoutput(cmd3)
	print result2

	#xx = r'\d{3,7}'
	xx = r'"patid": "\d{8,13}"'
	rex2 = re.compile(xx)
	patient_id_list = rex2.findall(result2)
	#print patient_id_list
	#print len(patient_id_list)

	search_list = []
	for patient_id in patient_id_list:
		#print patient_id
		if patient_id not in search_list:
			search_list.append(patient_id)
	#print search_list

	p_id_list = []
	for p_id in search_list:
		rex3 = re.compile(r'\d{8,13}')
		p_id = rex3.search(p_id).group()
		p_id_list.append(p_id)
	print p_id_list
	print 'The number of Ids those were searched is :',len(p_id_list)
	#for i in p_id_list:
		#if i in search_CT_number():
			#print 'The {} is : {}'.format(search_date,i) 
	return p_id_list

def check_CZ():       #
	a = serach_since()
	b = search_CT_number()
	print '-------------------------------------------------------------------'
	print 'it is not here',[l for l in b if l not in a]
	return [l for l in b if l not in a]

def check_folder_num():
	a = check_CZ()
	n = 0
	for i in a:
		print i,'#--------------------------------------------------------------------------'
		root = '/media/.../Data/DICOMS/CT'+'/{}'.format(i)
		#print 'patient:',os.listdir(root)
		for roots,dirs,files in os.walk(root):
			if len(files) > 0:
				print len(files)
		n += 1

	print 'Not Predicted num :',n
				


				








if __name__ == '__main__':
	#search_pid()
	#serach_since()
	#search_CT_number()
		#print i 
	#check_CZ()
	check_folder_num()


