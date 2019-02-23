# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 16:33:29 2019

@author: ahmad
"""

import pandas as p
import numpy as np

dataTrain = p.read_csv("D:\dappa titip\malin\TrainsetTugas1ML.csv") #mengambil data csv
dataTest = p.read_csv("D:\dappa titip\malin\TestsetTugas1ML.csv")

def ProbIncome(a):                                               #fungsi ini digunakan untuk menghitung probabilitas dari income
    j=0                                                          #variable untuk menyimpan jumlah data income berdasarkan kondisi
    i=0                                                          #variable untuk menyimpan jumlah data income
    for row in dataTrain.iloc[:,8].values:                       #perulangan untuk menentukan jumlah data dan jumlah data income berdasatkan kondisi antara ">50K" dan "<=50K"
        if row == a:
            j+=1
        i+=1
    return j,j/i                                                 #hasil output berupa nilai j dan probabilitas dari data income

def ProbData(a,b,c):                                             #fungsi ini dipakai untuk menghitung nilai probabilitas semua data dari tiap atribut terhadap atribut income
    j=0 
    i=0
    jum, income = ProbIncome(b)
    for row in dataTrain.iloc[:,c].values:                       #melakukan perulangan untuk menentukan nilai probabilitas dari tiap atribut (id,age, workclass, dll) yang termasuk dalam kategori >50k/<=50k
        if row == a and dataTrain.iloc[:,8].values[i] == b:      #kondisi berdasar row yang dipilih sesuai input dan nilai input pada kolom income
            j+=1
        i+=1
    return j/jum

exportCSV = []  #digunakan untuk menjadikan output program ke bentuk file csv

for i in range(0,40):                                           #perulangan ini digunakan untuk menguji data testing dengan data training untuk mendapatkan nilai income yang sesuai
    iT = ">50K"
    x,y = ProbIncome(iT)
    iTol = "<=50K"
    a,b = ProbIncome(iTol)
    row = dataTest.iloc[i,:].values
    terima = ProbData(row[1], iT, 1)*ProbData(row[2], iT, 2)*ProbData(row[3], iT, 3)*ProbData(row[4], iT, 4)*ProbData(row[5], iT, 5)*ProbData(row[6], iT, 6)*ProbData(row[7], iT, 7)*y
    tolak = ProbData(row[1], iTol, 1)*ProbData(row[2], iTol, 2)*ProbData(row[3], iTol, 3)*ProbData(row[4], iTol, 4)*ProbData(row[5], iTol, 5)*ProbData(row[6], iTol, 6)*ProbData(row[7], iTol, 7)*b
    
    if terima > tolak:                                          #untuk menentukan nilai yang sesuai dengan tiap data testing, apabila nilai probabilitas lebih tinggi akan menghasilkan output >50k begitupun sebaliknya
        #print(">50K")
        exportCSV.append(">50K")
    else:
        #print("<=50K")
        exportCSV.append("<=50K")

d = np.asarray(exportCSV)       
d.tofile('TebakanTugas1ML.csv', sep = '\n', format = '%s')
    
