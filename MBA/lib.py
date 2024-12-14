import os, csv
from gdown import download

# Função cria um diretorio    
def verificar_diretorio(nome_diretorio:str):
    if not os.path.exists(nome_diretorio):
        os.mkdir(nome_diretorio)
    return None


# Definir a função download_from_drive
def download_dataset(link,filename):
    file_id = link.split('/')[-2]
    url = f'https://drive.google.com/uc?id={file_id}'
    download(url, filename, quiet = False)
    return None

#Função que 
def preencher_matriz_contratos(nome_arquivo: str):
    matriz = []
    with open(nome_arquivo, 'r') as arquivo:

        # Lê as dimensões da matriz
        m, n, t = map(int, map(float, arquivo.readline().split()))

        # Inicializa a matriz com valores infinitos
        matriz = []
        for _ in range(n):
            camada = []
            for _ in range(m+1):
                linha = []
                for _ in range(m+1):
                    linha.append(float('inf'))
                camada.append(linha)
            matriz.append(camada)

        # Preenche a matriz com os valores dos contratos
        for linha in arquivo:
            fornecedor, inicio, fim, valor = map(float, linha.split())
            # Atribuindo o valor de contratos usando os indices declarados e retirando 1 do indice fornecedor para manter a indexação do python em 0
            matriz[int(fornecedor) - 1][int(inicio)][int(fim)] = valor 
    return m, n, t, matriz

def imprimir_matriz(matriz, k=None):
    if k is None:
        for i in range(len(matriz)):
            print(" ".join(str(elemento) for elemento in matriz[i]))# Utilizei o join para melhorar um pouco a visualização da matriz
            print()
    else:
        print(matriz[k])
    return None

def exportar_csv(nome_arquivo, matriz):
    with open(nome_arquivo, 'w', newline = '') as arq_csv:
        # Definindo contador inicial
        contador: int = 1
        # Adicionando a matriz no arquivo
        for bloco in matriz[1:]:
            csv.writer(arq_csv).writerow([f'Valores do fornecedor: {contador}'])
            csv.writer(arq_csv, delimiter=',').writerows(bloco)
            contador+=1
    
    print(f"O arquivo {nome_arquivo} foi criado com sucesso na pasta!")
    return None