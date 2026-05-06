{\rtf1\ansi\ansicpg1252\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import itertools\
from itertools import filterfalse\
dict001 = [1,2,3,4,5,6,7,8,9,0];\
\
\
dict004 = \{"name":"Alok","class":"1st","roll-number":30,"address":"Indore"\},\
\
print("-----------------------------------dict001---------------------------------------------")\
print("         --------------------Dict001 MAP Function--------------------------            ")\
\
resDict001 = list(map(lambda x :x+100 , dict001))\
print("resDict001:",resDict001);\
\
print("         --------------------Dict001 Filter Function-----------------------            ")\
\
res001Dict001 = list(filter(lambda x : x > 5,dict001))\
print("res001Dict001",res001Dict001);\
\
print("----------------------------------dict002-----------------------------------------------")\
dict002 = [\
            \{"name":"Alok","class":"1st","roll-number":30,"address":"Indore"\},\
            \{"name":"Ankur","class":"2st","roll-number":50,"address":"Delhi"\},\
            \{"name":"Amit","class":"3st","roll-number":20,"address":"Mumbai"\},\
            \{"name":"Annu","class":"4st","roll-number":60,"address":"Gwalior"\},\
            \{"name":"Aman","class":"5st","roll-number":90,"address":"Noida"\},\
           ];\
print("         ---------------------Dict002 Map Function(Change All Roll number)------------------------              ")\
\
resDict002 = list(map(lambda x :\{**x,"roll-number":x["roll-number"]+1000\},dict002))\
print("resDict002:",resDict002);\
\
print("       ---------------------Dict002 Filter Function--------------------              ");\
resDict002Filter = list(filter(lambda x: x["roll-number"] > 40, dict002));\
print("resDict002Filter:",resDict002Filter);\
\
print("      -------------------Dict002 filterFalse Function-----------------               ");\
resDict002FilterFalse = list(filterfalse(lambda x : x["roll-number"] > 40,dict002));\
print("resDict002FilterFalse:",resDict002FilterFalse);\
\
print("-------------------------Dict003--------------------------------------------------------");\
dict003 = \{\
            "customerName":\{"Fname":"Alok","Lname":"Chhari"\},\
            "ID":328001,\
            "itemPurchase":\{"Brand":"Dell","ItemType":"Laptop","Model":"Vostro-2542"\},\
            "Location":"Indore",\
            "purchaseId":2233432\
           \};\
print("              --------------------dict003 MAP function----------------------              ");\
resDict003Map = list(map(lambda x : x["ID"],[dict003]));\
print("resDict003Map:",resDict003Map);\
resDict003MapAnotherExample = list(map(lambda x: x["customerName"],[dict003]));\
print("resDict003MapAnotherExample:",resDict003MapAnotherExample);\
resDict003MapAnotherExample002 = list(map(lambda x: x["customerName"]["Fname"],[dict003]));\
print("resDict003MapAnotherExample002:",resDict003MapAnotherExample002)\
print("              --------------------another way to access (Fname Alok)-----------            ");\
print("Fname:", dict003["customerName"]["Fname"]);\
\
\
}