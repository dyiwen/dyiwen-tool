#!usr/bin/env python
# -*-coding:utf-8-*-

import os,time,re,commands

#----------config_params----------------------------
channel = 'ct0'
cmd = 'docker ps -a | grep {}'.format(channel)
end_date = '2018-07-10'
search_date = 'Jul 11'
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
	number_list = [patient_id[60:] for patient_id in search_list]
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
	cmd3 = 'docker logs -f -t --since={} {}'.format(since_date,PID)
	print cmd3

	result2 = commands.getoutput(cmd3)
	print result2
	'''
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
			#print 'The {} is : {}'.format(search_date,i) '''





if __name__ == '__main__':
	#search_pid()
	#serach_since()
	#search_CT_number()
		#print i 

	a = commands.getoutput('ping 192.168.1.1')
	b = os.popen('ping 192.168.1.1').read()
	print b


