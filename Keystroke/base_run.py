# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:48:45 2020

@author: Shreya Khuwal
"""
import os                                                                       
from multiprocessing import Pool                                                
                                                                                
f=open("try.txt",'w')
f.close()
processes = ('keylogger2.py','interface.py')                                    
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
if __name__ == "__main__":                                                                               
   __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"                                                                             
   pool = Pool(processes=2)                                                        
   pool.map(run_process, processes)  
