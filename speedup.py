import numpy as np
import pandas as pd

# Função para remover outliers com base no IQR
def remover_outliers(dados):
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1
    lim_inf = q1 - 1.5 * iqr
    lim_sup = q3 + 1.5 * iqr
    dados_filtrados = [x for x in dados if lim_inf <= x <= lim_sup]
    return dados_filtrados

# Lê os arquivos de tempo
tempos_sequencial = []
tempos_MPI = []
speedupList = []

with open('lista_tempo_sequencial.txt', 'r') as arq:
    tempos_sequencial = [float(linha.strip()) for linha in arq]

with open('lista_tempo_MPI.txt', 'r') as arq:
    tempos_MPI = [float(linha.strip()) for linha in arq]

# Remove outliers
tempos_sequencial_filtrados = remover_outliers(tempos_sequencial)
tempos_MPI_filtrados = remover_outliers(tempos_MPI)

# Calcula a média dos tempos filtrados
media_sequencial = np.mean(tempos_sequencial_filtrados)
media_MPI = np.mean(tempos_MPI_filtrados)

# Calcula o speedup
speedup = media_sequencial / media_MPI

# Exibe os resultados
print(f'Tempo medio Sequencial (sem outliers): {media_sequencial:.4f} segundos', flush= True)
print(f'Tempo medio MPI (sem outliers): {media_MPI:.4f} segundos', flush= True)
print(f'Speedup: {speedup:.4f}', flush= True)

# Salvar os resultados em um arquivo
def salvar_speedup(nprocs):
    with open('speedup_resultados.txt', 'a') as arq:
        arq.write(f'Tempo medio Sequencial (sem outliers): {media_sequencial:.4f} segundos\n')
        arq.write(f'Tempo medio MPI (sem outliers): {media_MPI:.4f} segundos\n')
        arq.write(f'Speedup: {speedup:.4f}\n')
        
    if nprocs == 2:
        with open('speedup_res_2.txt', 'a') as arq:
            arq.write(f'{speedup:.4f} \n')
    elif nprocs == 4:
        with open('speedup_res_4.txt', 'a') as arq:
            arq.write(f'{speedup:.4f} \n')
    elif nprocs == 5:
        with open('speedup_res_5.txt', 'a') as arq:
            arq.write(f'{speedup:.4f} \n')
    elif nprocs == 10:
        with open('speedup_res_10.txt', 'a') as arq:
            arq.write(f'{speedup:.4f} \n')
    elif nprocs == 20:
        with open('speedup_res_20.txt', 'a') as arq:
            arq.write(f'{speedup:.4f} \n')
    elif nprocs == 25:
        with open('speedup_res_25.txt', 'a') as arq:
            arq.write(f'{speedup:.4f} \n')
    elif nprocs == 50:
        with open('speedup_res_50.txt', 'a') as arq:
            arq.write(f'{speedup:.4f} \n')
            


def speedup_media(nprocs):
    if nprocs == 2:
        with open('speedup_res_2.txt', 'r') as arq:
            speedupList = [float(linha.strip()) for linha in arq if linha.strip()]
    elif nprocs == 4:
        with open('speedup_res_4.txt', 'r') as arq:
            speedupList = [float(linha.strip()) for linha in arq if linha.strip()]
    elif nprocs == 5:
        with open('speedup_res_5.txt', 'r') as arq:
            speedupList = [float(linha.strip()) for linha in arq if linha.strip()] 
    elif nprocs == 10:
        with open('speedup_res_10.txt', 'r') as arq:
            speedupList = [float(linha.strip()) for linha in arq if linha.strip()] 
    elif nprocs == 20:
        with open('speedup_res_20.txt', 'r') as arq:
            speedupList = [float(linha.strip()) for linha in arq if linha.strip()]
    elif nprocs == 25:
        with open('speedup_res_25.txt', 'r') as arq:
            speedupList = [float(linha.strip()) for linha in arq if linha.strip()] 
    elif nprocs == 50:
        with open('speedup_res_50.txt', 'r') as arq:
            speedupList = [float(linha.strip()) for linha in arq if linha.strip()]
    else: 
        print("numero de processsos invalidos")
        return

    speedup_media = np.mean(speedupList)
    print(f"media de speedup de {nprocs} processos:{speedup_media:.4f}")
    

