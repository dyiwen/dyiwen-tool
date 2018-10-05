#!/usr/bin/python
# -*- coding: utf-8 -*-
from easydict import EasyDict as edict

config = edict()
config.IMAGE_ROOT = "/home/.../Downloads/test_data_dicom/"
#config.IMAGE_ROOT = "/media/.../Data/DICOMS/CT/"

config.Patient_Path = '1515037607'

config.RESULT_ROOT = "/media/.../Data/output/CT/"
config.JSON_ROOT = "/media/.../Data/json/"
config.channel = "CT0"
config.interval_seconds = 30
