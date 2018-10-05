#!usr/bin/env python
# -*-coding:utf-8-*-

import os,time,re,commands

#----------config_params----------------------------
channel = 'ct0'
cmd = 'docker ps -a | grep {}'.format(channel)
end_date = '2018-07-15'
search_date = 'Jul 16'
since_date = '"2018-07-16"'



def search_use_time():

#--------------------------------------------
	result1 = os.popen(cmd).read()
	print result1
	#rex = re.compile(r'[\a-z0-9]{12}')
	rex = re.compile(r'\w{12}')
	PID = rex.search(result1).group()
	print PID
#---------------------------------------------
	cmd1 = 'docker logs -t --since={} {}'.format(since_date,PID)
	print cmd1
	result2 = commands.getoutput(cmd1)
	print result2

	xx = r'Total time \d{2,11}'
	rex = re.compile(xx)
	dl_use_time = rex.findall(result2)
	print dl_use_time
	print 'the num of predictied is :',len(dl_use_time)


if __name__ == '__main__':
	search_use_time()
