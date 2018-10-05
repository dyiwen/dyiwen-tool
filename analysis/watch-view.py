# -*- coding:utf8 -*-
# !/usr/bin/env python

import pydicom
import pylab
import time
import os

#path = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data/two-dicom/0001614904/1.2.840.113704.1.111.4356.1530064458.1/1.2.840.113704.1.111.4356.1530064617.16'
#头部
#path = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data/two-dicom/0001614904/1.2.840.113704.1.111.4356.1530064458.1/1.2.840.113704.1.111.4356.1530064613.11'

#path = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data/lots/0001660692/1.2.840.113704.1.111.3760.1530063876.1/1.2.840.113704.1.111.3760.1530064155.21'
path_1 = '/media/dyiwen/KINGSTON/tuomin/6-27nanchang/wenti-dicom-data/two-dicom/0001614904/1.2.840.113704.1.111.4356.1530064458.1/1.2.840.113704.1.111.4356.1530064617.16/1.2.840.113704.1.111.3552.1530064736.9843.dcm'
#path_2 = '/media/tx-deepocean/Data/DICOMS/CT/0001703839/1.3.46.670589.33.1.63667444961053760700001.4985133490430371683/1.3.46.670589.33.1.63667445057989305100001.5396394762883265582/1.3.46.670589.33.1.63667445309324680700001.5763723852784861540.dcm'
path_2 = "/media/dyiwen/Seagate Expansion Drive/gupen/0001695626/1.2.840.113704.1.111.6460.1532141511.1/1.2.840.113704.1.111.6460.1532141799.23/1.2.840.113704.1.111.2992.1532141817.11211.dcm"
def signal_dicom(path):
    ds = pydicom.read_file(path)
    pexel_bytes = ds.PixelData
    pix = ds.pixel_array
    pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
    pylab.show()

def for_dicom(path):
    n = 0
    for file in os.listdir(path):
        #print file
        ds = pydicom.read_file(path+'/'+file)
        pexel_bytes = ds.PixelData
        pix = ds.pixel_array
        pylab.imshow(pix,cmap=pylab.cm.bone)
        pylab.show()
        n += 1
        print n

def ds_read(path):
    ds = pydicom.read_file(path)
    print ds.dir()
    print ds.ProtocolName
    a = ds.ProtocolName
    if ds.ProtocolName == 'NC Pelvis Helical 1mm/Pelvis':
        print 'True'
    else:
        print 'Flase'





if __name__ == '__main__':
    #for_dicom(path_2)
    #signal_dicom()

    ds_read(path_2)