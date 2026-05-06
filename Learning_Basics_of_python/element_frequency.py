{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 tup1 = (1,1,2,2,7,0,7,6,6,6,5,5,5,5,0,0,0,0,4,2,4,4,8,8,9,1,4,0,2,3,3,5,5,6,0,1);\
listTup2 = list(tup1);\
listTup2.sort(reverse=False);\
getNumberCount = [(numbers,listTup2.count(numbers)) for numbers in listTup2];\
print(set(getNumberCount));}