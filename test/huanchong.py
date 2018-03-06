# coding=utf-8
'''
Created on 2018年3月4日

@author: xiaoyuer
'''
import re
from _codecs import decode
 

filename1 = "d:\\a.txt"
try:
    with open(filename1) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry ,the file" + filename1+ "doesn't exist !"
    print(msg)
else :
    words =re.split(' |\?|\.|!|。|,|，|\？|！',contents)
    while '\n' in words:
        words.remove('\n')
    while '' in words:
        words.remove('')
    num_words = len(words)
    print("the file" + filename1 + " has +about "+ str(num_words) + "words .")
        
    



