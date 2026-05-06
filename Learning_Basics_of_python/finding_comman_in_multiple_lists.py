{\rtf1\ansi\ansicpg1252\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97without counter function \'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
\
list001 = [1,2,3,4,10,8,6,1,1,1,1,1,1];\
list002 = [5,5,5,5,6,7,3,8,4,10,8,6];\
list003 = [9,10,3,11,4,12,10,];\
\
combineList = [list001 , list002 , list003];\
print(combineList);\
\
collectiveList = list(set(list001)) + list(set(list002)) + list(set(list003));\
\
res = list(map(lambda x: (x,collectiveList.count(x)) , collectiveList))\
print(res);\
\
res001 = set(filter(lambda x : x[1] >= len(combineList), res));\
print(res001);\
\
res002 = list(map(lambda x : x[0],res001))\
print(res002)\
\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97using counter function from collections\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
\
from collections import Counter\
list001 = [1,2,3,4,10,8,6,1,1,1,1,1,1];\
list002 = [5,5,5,5,6,7,3,8,4,10,8,6];\
list003 = [9,10,3,11,4,12,10,];\
\
collectiveList  = list(set(list001)) + list(set(list002)) + list(set(list003));\
print("collective List:",collectiveList)\
print("-------------------------------001------------------------");\
\
reOccour = Counter(collectiveList);\
print("Re Occour:",reOccour)\
print("-------------------------------002------------------------");\
\
countList = [list001 , list002 , list003];\
print("Count List:",len(countList));\
print("-------------------------------003------------------------");\
\
resultTuple = list(filter(lambda x : x[1] == len(countList) ,  reOccour.items()))\
print("resultant Tuple:",resultTuple)}