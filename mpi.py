from mpi4py import MPI
import numpy as np
import csv
import sys
import crudArq


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
matriz1= None
matriz2= None
quantLin_1 = None
quantCol_1 = None
if rank == 0:
    with open('matriz1.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv) 
        matriz1 = np.array([list(map(int,linha)) for linha in leitor_csv])

    with open('matriz2.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        matriz2 = np.array([list(map(int, linha)) for linha in leitor_csv])

    quantLin_1 = len(matriz1)
    quantCol_1 = len(matriz1[0])
    quantLin_2 = len(matriz2)
    quantCol_2 = len(matriz2[0])


    if(quantCol_1 != quantLin_2):
        print("matrizes de formato incompativel para a realizacao da operacao")
        sys.exit()

    
    if quantLin_1 % nprocs != 0 :
        print("numero de processos incorreto")
        sys.exit()

(quantLin_1, quantCol_1) = comm.bcast((quantLin_1, quantCol_1), root = 0)

#Cria um array, no formato de linhas que cada processo vai receber, sem inicializar
submatriz1 = np.empty((quantLin_1 // nprocs , quantCol_1), dtype= int)

comm.Scatterv(matriz1, submatriz1, root= 0)


#Envia a matriz 2 para todos os processos
matriz2= comm.bcast(matriz2, root = 0)  


#cada processo calcula a sua parte da multiplicação
submatrizRes = np.matmul(submatriz1, matriz2)

matrizRes = None


if rank == 0 :
    matrizRes = np.empty((quantLin_1, quantCol_2), dtype= int)


#if rank == 0:
#    print("MatrizRes shape:", matrizRes.shape)
#    print("SubmatrizRes shape:", submatrizRes.shape)


#Reune os trechos calculados pelos ranks em matrizRes    
comm.Gatherv(submatrizRes,matrizRes, root = 0)



if rank == 0:
    crudArq.salvarResultadoMPI(matriz_res= matrizRes)




