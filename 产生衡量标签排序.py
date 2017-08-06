#coding=utf-8
import os,sys
from operator import itemgetter
global dabiaoqian
global list1
global j
j=0
list1=[]
for zoudao in ['AA','BB']:                                          #走道
    for shuzi in range(21,99):                                      #范围
        jiou=shuzi%2
        for cengshu in ['A','B','C','D']:                           #层数
            for xshuzi in ['1','2','3','4']:                        #具体料位
                biaoqian = zoudao+'0'+str(shuzi)+cengshu+xshuzi
                list1+=[{'zoudao':zoudao,'shuzi':shuzi,'cengshu':cengshu,'xshuzi':xshuzi,'jiou':jiou}]             
# print str(list1) 
list2=sorted(list1,key=itemgetter('zoudao','jiou','cengshu','shuzi','xshuzi'))          #排序
# print str(list2[0]['zoudao'])
for i in list2:
    str1=str(list2[j]['zoudao']+'0'+str(list2[j]['shuzi'])+list2[j]['cengshu']+list2[j]['xshuzi'])
    j=j+1
    f=open(sys.path[0]+r'\loc.txt','a+')                #当前路径生成txt
    f.write(str1+'\n')
    f.close()

# os.system(r'c:\')
os.system(sys.path[0]+'\批次产生料位检查码.exe')
# print sys.path[0]
print ' '
print 'OVER'
