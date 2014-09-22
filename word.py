# -*- coding: utf-8 -*-
import win32com
import os,sys
import os.path
from shutil import copy




import os
def walk_dir(dir,topdown=True):

    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            if ('doc'in name) or ('docx' in name):
                fullpath=root+'\\'+name
                print fullpath
                print '------'
                copy(fullpath, ur'D:\copy')
                


        
        


if __name__ == '__main__':
    walk_dir(ur"E:\360data\重要数据\我的文档\BaiduYunPan\工作\支队\船艇资料汇总")