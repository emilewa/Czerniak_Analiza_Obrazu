# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:09:55 2020

@author: emilk


Legends for Clinical Diagnosis: 
   0 - Common Nevus;
   1 - Atypical Nevus;
   2 - Melanoma.

Legends for Asymmetry: 
   0 - Fully Symmetric;
   1 - Symetric in 1 axe;
   2 - Fully Asymmetric;

Legends for Pigment Network, Dots/Globules, Streaks, Regression Areas, and Blue-Whitish Veil: 
   A  - Absent;
   AT - Atypical;
   P  - Present;
   T  - Typical.

Legends for Colors: 
   1 - White;
   2 - Red;
   3 - Light-Brown;
   4 - Dark-Brown;
   5 - Blue-Gray;
   6 - Black.

"""
from konturyFunkcjeParametry import *
import csv
import os



         
         
class dane:
    name             = ""
    hist_diagnosis   = ""
    clinic_diagnosis = ""
    asymmetry        = ""
    pigment          = ""
    dots_globules    = ""
    streaks          = ""
    regression_area  = ""
    veil             = ""
    colors           = ""
    White = "0"
    Red = "0"
    Light_Brown = "0"
    Dark_Brown = "0"
    Blue_Gray = "0"
    Black = "0"
    cx = ""
    cy = ""
    Pole = "" 
    L = "" 
    solidity = ""
    wypuklosc = 0
    szer_wys = ""
    W9 = ""
    #struct = ''
#    struct = {  'Name'                    : name,
#                'Histological_Diagnosis'  : hist_diagnosis ,
#                'Clinical_Diagnosis'      : clinic_diagnosis,
#                'Asymmetry'               : asymmetry,
#                'Pigment_Network'         : pigment,
#                'Dots/Globules'           : dots_globules,
#                'Streaks'                 : streaks,
#                'Regression_Areas'        : regression_area,
#                'Blue_Whitish_Veil'       : veil,
#                'White'                   : White,
#                'Red'                     : Red,
#                'Light_Brown'             : Light_Brown,
#                'Dark_Brown'              : Dark_Brown,
#                'Blue_Gray'               : Blue_Gray,
#                'Black'                   : Black,
#                'Area'                    : Pole,
#                'Circuit'                 : L,
#                'Solidity'                : solidity,
#                'Convex'                  : wypuklosc,
#                'Aspect_Ratio'            : szer_wys,
#            }
#    
    
    def __init__(self,row):
        
         self.name             = row[0].split()[0]
         self.hist_diagnosis   = row[1].lstrip()
         self.clinic_diagnosis = row[2].split()[0]
         self.asymmetry        = row[3].split()[0]
         self.pigment          = row[4].split()[0]
         self.dots_globules    = row[5].split()[0]
         self.streaks          = row[6].split()[0]
         self.regression_area  = row[7].split()[0]
         self.veil             = row[8].split()[0]
         self.colors           = row[9].split()
         self.PrzypiszKolory()
         self.OdczytajMaske()
    
    def Struct(self):      
         struct = {       
                          'Name'                    : self.name,
                          'Histological_Diagnosis'  : self.hist_diagnosis ,
                          'Clinical_Diagnosis'      : self.clinic_diagnosis,
                          'Asymmetry'               : self.asymmetry,
                          'Pigment_Network'         : self.pigment,
                          'Dots/Globules'           : self.dots_globules,
                          'Streaks'                 : self.streaks,
                          'Regression_Areas'        : self.regression_area,
                          'Blue_Whitish_Veil'       : self.veil,
                          'White'                   : self.White,
                          'Red'                     : self.Red,
                          'Light_Brown'             : self.Light_Brown,
                          'Dark_Brown'              : self.Dark_Brown,
                          'Blue_Gray'               : self.Blue_Gray,
                          'Black'                   : self.Black,
                          'Area'                    : self.Pole,
                          'Circuit'                 : self.L,
                          'Solidity'                : self.solidity,
                          'Convex'                  : self.wypuklosc,
                          'Aspect_Ratio'            : self.szer_wys,
                          'W9'                      : self.W9
                          }
         return struct
                         
    def PrzypiszKolory(self):
        for r in self.colors:
            if r=='1':
                self.White = '1'
            elif r=='2':
                self.Red = '1'
            elif r=='3':
                self.Light_Brown = '1'
            elif r=='4':
                self.Dark_Brown = '1'
            elif r=='5':
                self.Blue_Gray = '1'
            elif r=='6':
                self.Black = '1'
                
    def OdczytajMaske(self):
        #PH2/IMD002/IMD002_lesion/IMD002_lesion.bmp
        sciezka = "PH2/"+self.name + "/"+self.name+"_lesion/"+self.name+"_lesion.bmp"
        print(sciezka)
        if os.path.isfile(sciezka):
            print("Znalazlo maske obrazu "+self.name)
            im = cv2.imread(sciezka)
            imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            cx, cy, Pole, L, solidity, wypuklosc, szer_wys, W9 = momenty(imgray)
            self.cx = cx
            self.cy = cy
            self.Pole = Pole
            self.L = L
            self.solidity = solidity
            self.wypuklosc = wypuklosc
            self.szer_wys = szer_wys
            self.W9 = W9
            
    def TworzeDaneDoTrenowaniaSieci(self):
            #PH2/IMD002/IMD002_lesion/IMD002_lesion.bmp
            sciezka = "PH2/"+self.name + "/"+self.name+"_lesion/"+self.name+"_lesion.bmp"
            sciezka_zapisu_label = "data/membrane/train/label/"+self.name+".png"
            print(sciezka)
            if os.path.isfile(sciezka):
                print("Znalazlo maske obrazu "+self.name)
                print("Sciezka obrazu : "+sciezka)
                print("Sciezka zapisu : "+sciezka_zapisu_label)
                im = cv2.imread(sciezka)
                cv2.imwrite(sciezka_zapisu_label,im)
            
            sciezka_obraz = "PH2/"+self.name + "/"+self.name+"_Dermoscopic_Image/"+self.name+".bmp"
            sciezka_zapisu_obrazu = "data/membrane/train/image/"+self.name+".png"
            
            if os.path.isfile(sciezka_obraz):
                print("Znalazlo obraz "+self.name)
                print("Sciezka obrazu : "+sciezka_obraz)
                print("Sciezka zapisu : "+sciezka_zapisu_obrazu)
                im = cv2.imread(sciezka_obraz)
                cv2.imwrite(sciezka_zapisu_obrazu,im) 
            

def doCSV(lista):
        
    with open('plik.csv', 'w', newline="") as csvfile2:
    # definiujemy nagłówek (czyli nasze kolumny)
        fieldnames = ['Name','Histological_Diagnosis','Clinical_Diagnosis','Asymmetry','Pigment_Network','Dots/Globules','Streaks','Regression_Areas','Blue_Whitish_Veil','White','Red','Light_Brown','Dark_Brown','Blue_Gray','Black','Area','Circuit','Solidity','Convex','Aspect_Ratio','W9']
       
        #csvwriter2 = csv.DictWriter(csvfile2, delimiter=';')
        csvwriter2 = csv.DictWriter(csvfile2, restval='', delimiter=',', fieldnames=fieldnames)
    
        # zapisujemy do pierwszej linii zdefiniowane wczesniej nazwy kolumn
        csvwriter2.writeheader()
    
        # zapisujemy do pliku po kolei nasze struktury iterujac po ich liscie
        for n in lista:
            csvwriter2.writerow(n.Struct())
            
            
            
    
def zCSV(lista):
    with open('dane.csv', 'r') as csvfile:
        # deklarujemy nasz *czytacz*
        # parametr *delimiter* jest opcjonalny i wskazuje jaki został w pliku użyty separator
        csvreader = csv.reader(csvfile, delimiter=';')        
        
        i=0
        for row in csvreader:            
            r = dane(row)
            r.TworzeDaneDoTrenowaniaSieci()
            if i>0 :
                lista.append(r)    
            i = i+1



         
         
lista = []         
zCSV(lista)
doCSV(lista)

#
#i = 1
#for v in lista:
#    print(str(i) +"  "+v.name)
#    i = i+1 
    