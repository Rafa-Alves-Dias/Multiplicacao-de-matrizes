import numpy as np
import csv
import pandas as pd

def gerarMatrizes():
    dim_matriz1 = (1000, 900)
    dim_matriz2 = (900, 1000)

    matriz1 = np.random.randint(0, 100, size = dim_matriz1)
    matriz2 = np.random.randint(0, 100, size = dim_matriz2)

    matriz1_df = pd.DataFrame(matriz1)
    matriz2_df = pd.DataFrame(matriz2)

    matriz1_df.to_csv('matriz1.csv', index = False, header = False)
    matriz2_df.to_csv('matriz2.csv', index = False, header = False)


def salvarResultadoSeq(matriz_res):
    with open('matriz_res_sequencial.csv', 'w', newline='') as  arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(matriz_res)


def salvarResultadoMPI(matriz_res):
    with open('matriz_res_MPI.csv', 'w', newline='') as  arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(matriz_res)


def limparArq():
    with open('matriz_res_MPI.csv', 'w') as file:
        pass

    with open('matriz_res_sequencial.csv', 'w') as file:
        pass

    with open('lista_tempo_MPI.txt', 'w') as file:
        pass

    with open('lista_tempo_sequencial.txt', 'w') as file:
        pass