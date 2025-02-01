import subprocess
import time 
import crudArq
import os
import speedup

crudArq.gerarMatrizes()
crudArq.limparArq()

script_sequencial = 'sequencial.py'
script_MPI = 'mpi.py'

num_execucoes = 50
nprocs = 2

def executar_sequencial(script):
    inicio = time.perf_counter()
    subprocess.run(['python', script], check = True)
    fim = time.perf_counter()
    return fim - inicio

def executar_MPI(script, nprocs):
    inicio = time.perf_counter()
    subprocess.run(['mpiexec', '-n', str(nprocs), 'python', script], check = True)
    fim = time.perf_counter()
    return fim - inicio

def executar_speedup():
    subprocess.run(['python', 'speedup.py'], check = True)

tempos_sequencial = []
tempos_MPI = []

for i in range(num_execucoes):
    print(f'Execucao {i + 1} / {num_execucoes} - Sequencial', flush = True)
    tempo =  executar_sequencial(script_sequencial)
    tempos_sequencial.append(tempo)

    print(f'Execucao {i + 1} / {num_execucoes} - MPI', flush = True)
    tempo = executar_MPI(script = script_MPI, nprocs = nprocs)
    tempos_MPI.append(tempo)

with open('lista_tempo_sequencial.txt', 'a') as arq:
    for tempo in tempos_sequencial:
        arq.write(f'{tempo} \n')
        arq.flush()

with open('lista_tempo_MPI.txt', 'a') as arq:
    for tempo in tempos_MPI:
        arq.write(f'{tempo} \n')
        arq.flush()

executar_speedup()

def speedup_com_nprocs(nprocs):
    speedup.salvar_speedup(nprocs= nprocs)
    speedup.speedup_media(nprocs= nprocs)


speedup_com_nprocs(nprocs= nprocs)