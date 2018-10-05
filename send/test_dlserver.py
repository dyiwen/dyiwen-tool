#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################
### 说明： 
### 本测试文件用于测试DL Server。
##############################  
import json
import redis
import os
import time
from config import config


# Send analyze request via Redis to dlserver
def send_request(redis_client, channel, src_dir, dst_dir, f):
    hjson = {}
    # path 指代影像号的图像文件夹存储路劲
    hjson["image_path"] = src_dir
    hjson["save_path"] = dst_dir
    hjson["json_path"] = config.JSON_ROOT

    # 通过Redis，向dl server发出分析指令
    redis_client.publish(channel, json.dumps(hjson))
    print f, "publish finished!"


# Send analyze requests for a list of folder to dlserver
def send_request_per_folder(redis_client, channel, image_dir, save_dir, time_interval):
    for f in os.listdir(image_dir):
        src_dir = os.path.join(image_dir, f)
        dst_dir = os.path.join(save_dir, f)
        send_request(redis_client, channel, src_dir, dst_dir, f) 
        time.sleep(time_interval)    


if __name__ == '__main__':
    r = redis.Redis()
    channel = config.channel
    #patient_id = "759110/1.2.840.1.19439.0.108707908.20180710133112.1197.10000.2815187/1.2.156.112605.14038001405059.20180710053111.3.3872.5"
    patient_id = config.Patient_Path
    image_dir = os.path.join(config.IMAGE_ROOT, patient_id)
    save_dir = os.path.join(config.RESULT_ROOT, patient_id)
    print image_dir
    start = time.time()
    send_request(r, channel, image_dir, save_dir, patient_id)
    end = time.time()
    print '------',image_dir[35:45]
    print "Total elapsed time: ", (end - start)
