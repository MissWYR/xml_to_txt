# -*- coding:utf-8 -*-
#作者：卫毅然（老卫）
#邮箱：2205492446@qq.com
#该脚本用于将xml文件转化为txt文件

import os
import sys
import xml.etree.ElementTree as ET
import glob

jpg_indir="/home/weiyiran/Public/esophagus_img/"

def xml_to_txt(indir,outdir):

    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')
    retval = os.getcwd()
    print(retval)
    print(annotations)
    f_w = open("/home/weiyiran/Documents/xml_to_txt/sample.txt", 'w')
    for i, file in enumerate(annotations):

        # file_save = file.split('.')[0]+'.txt'
        # file_txt=os.path.join(outdir,file_save)
        # f_w = open(file_txt,'w')

        # actual parsing
        in_file = open(file)
        tree=ET.parse(in_file)
        root = tree.getroot()

        file_name=file.split('.')[0]+".jpg"
        print(file_name)

        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text

                xmlbox = obj.find('bndbox')
                xn = xmlbox.find('xmin').text
                xx = xmlbox.find('xmax').text
                yn = xmlbox.find('ymin').text
                yx = xmlbox.find('ymax').text
                #print xn
                f_w.write(jpg_indir+file_name+',')
                f_w.write(xn+','+yn+','+xx+','+yx+',')
                f_w.write(str(name+"\n"))

indir='/home/weiyiran/Public/esophagus_label'   #xml目录
outdir='/home/weiyiran/Documents/xml_to_txt'  #txt目录

xml_to_txt(indir,outdir)



