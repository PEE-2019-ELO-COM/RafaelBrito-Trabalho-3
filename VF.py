# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:07:17 2019

@author: binks
"""
def CalcularVF(MVE,VC):
    VF = 10 - (MVE/2 + VC/2)
    return VF
    
def somar_elementos(lista):
  soma = 0
  for numero in lista:
    soma += numero
  return soma

import time
VE = []
PVE = []

NVEs = int(input('Olá, esse programa calculará a nota que precisa para a sua VF \nQuantas VEs voce teve? (Lembre-se que so numeros sao admitidos)\n'))
if(NVEs>=1): 
    for x in range (NVEs):
        print('Nota da VE',x+1,':')
        y = float(input())
        if (y<=10 and y>=0):    
            VE.append(y)
            print('Qual era o peso dessa VE?')
            y = float(input())
            PVE.append(y)
        else:
            print('A nota que colocou é maior que 10 ou menor que 0, insira novamente essa nota (se a nota realmente for maior que 10 ou menor que 0 por caracteristica do professor, so insira novamente)' )
            y = float(input())
            VE.append(y)
            print('Qual era o peso dessa VE?')
            y = float(input())
            PVE.append(y)

peso = 0
for x in range (NVEs):
    
    peso = peso + PVE[x]

print('Qual foi sua nota da VC?')
VC = float(input())
while (VC<=0 or VC>=10):
    print('O input de VC foi menor que 0 ou maior que 10, recoloque a nota')
    VC=float(input())
    
MVE=0
for i in range (NVEs):
    MVE = VE[i]*PVE[i] + MVE

MVE = MVE/peso

VF = CalcularVF(MVE,VC)
                    
if (VF < 4):
    print('Só precisa tirar 4! Boa Sorte!')
    time.sleep(5)
    sys.exit()
        
else: 
    print('Precisa tirar',round(VF,2),'Boa Sorte!')
    time.sleep(5)
    sys.exit()
        
    
    
    
    
    
    
    
    