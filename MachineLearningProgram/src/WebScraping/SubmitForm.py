#coding=gbk
'''
Created on 2016��4��23��

@author: Administrator
'''
import requests

params = {'firstname':'liu','lastname':'daiyuan'}
r = requests.post("http://pythonscraping.com/files/processing.php",data=params)
print(r.text)