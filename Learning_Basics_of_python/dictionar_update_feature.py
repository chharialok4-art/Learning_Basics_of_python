{\rtf1\ansi\ansicpg1252\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 dict003 = \{"name":"Viraj Singh","roll-no":21,"school":"St.norbert","Address":"Indore"\};\
print(dict003);\
print("------------------------------------002--------------------------------------------")\
makeUpdict = \{**dict003 , "name":"Vedansh Singh"\};\
print("MakeupDict:",makeUpdict);\
\
\
dict002 = [\
            \{"name":"Alok","class":"1st","roll-number":30,"address":"Indore"\},\
            \{"name":"Ankur","class":"2st","roll-number":50,"address":"Delhi"\},\
            \{"name":"Amit","class":"3st","roll-number":20,"address":"Mumbai"\},\
            \{"name":"Annu","class":"4st","roll-number":60,"address":"Gwalior"\},\
            \{"name":"Aman","class":"5st","roll-number":90,"address":"Noida"\},\
           ];\
res = list(map(lambda x : \{**x,"roll-number":x["roll-number"]+1000\},dict002));\
print(res);\
print("---------------------------------001---------------------------------------")}