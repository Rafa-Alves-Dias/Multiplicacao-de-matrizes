import numpy as np
import csv
import sys
import crudArq

with open('matriz1.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv) 
    matriz1 = [list(map(int,linha)) for linha in leitor_csv]

with open('matriz2.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    matriz2 = [list(map(int, linha)) for linha in leitor_csv]

quantCol_1 = len(matriz1[0])
quantLin_2 = len(matriz2)

if(quantCol_1 != quantLin_2):
    print("matrizes de formato incompativel para a realizacao da operacao")
    sys.exit()

matriz_res = np.matmul(matriz1, matriz2) # ou matriz1 @ matriz2

crudArq.salvarResultadoSeq(matriz_res= matriz_res)
