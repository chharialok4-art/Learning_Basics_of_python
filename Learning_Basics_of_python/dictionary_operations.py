{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 FMCGproduct = [\
    \{"name":"cinthol", "price":2000, "Brand":"Hindustan Unilever","quantity":20\},\
    \{"name":"Detol" , "price":1000, "Brand":"parle Agro","quantity":10\},\
    \{"name":"Lays" , "price":500, "Brand":"Hamdard","quantity":70\},\
    \{"name":"pepsi", "price":4000,"Brand":"pepsi","quantity":90\},\
    \{"name":"parle-G","price":600,"Brand":"parle","quantity":60\},\
    \{"name":"pinepple-cake","price":9000,"Brand":"Britania","quantity":40\},\
    \{"name":"Cancil","price":5000,"Brand":"Loriyal","quantity":60\},\
    \{"name":"RIN" , "price":2400,"Brand":"RIN","quantity":30\},\
    \{"name":"Lake-May","price":3400,"Brand":"Loriyal","quantity":50\},\
];\
\
AveQuant = \{"total price":None , "Average":None, "total quantitity":None, "average quantity":None\};\
\
getTotalPrice = sum(map(lambda x : x["price"],FMCGproduct));\
getPriceAverage = (getTotalPrice/len(FMCGproduct));\
getTotalQuantity = sum(map(lambda x : x["quantity"] , FMCGproduct));\
getQuantityAverage = (getTotalQuantity/len(FMCGproduct));\
AveQuant["total price"] = getTotalPrice;\
AveQuant["Average"] = getPriceAverage;\
AveQuant["total quantitity"] = getTotalQuantity;\
AveQuant["average quantity"] = getQuantityAverage;\
print("Records:",AveQuant);}