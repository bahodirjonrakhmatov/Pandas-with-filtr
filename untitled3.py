# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kQ4EYDfb6TvzdMHIGswsTWfj7XRkT8OO
"""

import pandas as pd
baza= {
    "FISH": ["Raxmatov Bahodirjon","Xalilov Durbek","Yoldashov Muhammadyusf","Raxmatov Bahromjon","Qadamova Zulayho","Aripov Rahmiddin","Olimov Rahmatjon","Kimsanboyov Kimsan","Teshaboyov Bolta","Qaxorova Jasmin"],
    "Manzil": [ "Quva tumani","Fargon shahar","Fargona tumani","Quva tuman","Fargona shahar","Quva tumani","Quva tumani","Toshkent shahar","Xorazim tumani","Toshkent shahar"],
    "Yoshi": ["19","70","19","14","28","40","62","19","25","20"],
    "Ish joyi": ["Yoq","TATUFF","Direktor", "61-maktab oquvchisi","TATUFF","Biznesmen","IIV","Usta","Bank xodimi","Farrosh" ],
    "Jinsi": ["Erkak","Erkak","Erkak","Erkak","Ayol","Erkak","Erkak","Erkak","Erkak","Ayol"]
}

db=pd.DataFrame(baza)
print(db)

filtr1=db[db["Jinsi"]=="Erkak"]
print(filtr1)

filtr2=db[db ["Ish joyi"]=="TATUFF"]
print(filtr2)

filtr3=db[db ["Yoshi"]>"19"]
print(filtr3)