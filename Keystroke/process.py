# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:51:01 2020

@author: Shreya Khuwal
"""
from collections import defaultdict
def categorize(chars):
    hand_1=leftright(chars[0])
    hand_2=leftright(chars[2])
    possibility={('l',False,'l',False):1,('l',True,'l',True):1,
              ('r',False,'r',False):2,('r',True,'r',True):2,
              ('l',False,'r',True):3,
              ('l',True,'r',False):4,
              ('r',False,'l',True):5,
              ('r',True,'l',False):6,
              ('l',False,'l',True):7,('l',True,'l',False):7,
              ('r',False,'r',True):8,('r',True,'r',False):8,
              ('l',False,'r',False):9,('l',True,'r',True):9,
              ('r',False,'l',False):10,('r',True,'l',True):10}
              
    possibility=defaultdict(lambda: 0,possibility)          
    
    return possibility[hand_1,chars[1],hand_2,chars[3]]
    
    
    
def leftright(x):
    dict={65:'l',66:'l',67:'l',68:'l',69:'l',70:'l',71:'l',72:'r',73:'r',
          74:'r',75:'r',76:'r',77:'r',78:'r',79:'r',80:'r',81:'l',82:'l',
          83:'l',84:'l',85:'r',86:'l',87:'l',88:'l',89:'r',90:'l',48:'r',
          49:'l',50:'l',51:'l',52:'l',53:'l',54:'r',55:'r',56:'r',57:'r',
          97:'l',98:'l',99:'l',100:'l',101:'l',102:'l',103:'l',104:'r',105:'r',
          106:'r',107:'r',108:'r',109:'r',110:'r',111:'r',112:'r',113:'l',114:'l',
          115:'l',116:'l',117:'r',118:'l',119:'l',120:'l',121:'r',122:'l',
          9:'l',20:'l',189:'r',187:'r',33:'l',34:'r',35:'l',36:'l',37:'l',38:'r',
          219:'r',221:'r',220:'r',186:'r',222:'r',188:'r',39:'r',40:'r',41:'r',42:'r',
          190:'r',191:'r',8:'b', 13:'E', 32:'S',43:'r',44:'r',45:'r',46:'r',47:'r'}
    return dict.get(x,'n')
    
    
def lr_holdtime(x):
    
    possibility={('E',False):1,('E',True):1,('S',False):2,('S',True):2 ,
              ('l',False):3,('l',True):4,('r',False):5,('r',True):6}
    
    possibility=defaultdict(lambda: 0,possibility)
    
    return possibility[leftright(x[0]),x[1]]