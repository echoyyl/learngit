'''
Created on 2018年1月13日

@author: ClumsyCat
'''
#计算某个文件中的单词个数
import re

filename = input('请输入要创建的文件名，以用于后面计算其中的单词个数：')
contents = input('请输入文件的内容：')
try:
    with open(filename,'w') as fileWriter:
        fileWriter.write(contents)
except:
    print('发生错误！')
else:
    print('文件内容写入成功！')

try:
    with open(filename) as fileReader:
        contents = fileReader.read()
except:
    print(filename+'不存在，请输入正确的文件名或使用绝对路径！')
else:
    words = re.split(' |\?|\.|!|。|,|，|\？|！', contents)
    while '\n' in words:
        words.remove('\n')
    while '' in words:
        words.remove('')
    num = len(words)
    print('该文件中的单词个数为：'+str(num))
