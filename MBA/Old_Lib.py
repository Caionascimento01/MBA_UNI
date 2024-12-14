import os, csv
from gdown import download
import numpy as np

# Função para realizar o download do arquivo
def download_dataset(link: str, nome_arquivo: str):
    """
    Realizar o download do arquivo de dados
    """
    # Colentando o ID do arquivo
    id_arquivo = link.split('/')[5]

    # Definindo a URL de download
    url = f'https://drive.google.com/uc?id={id_arquivo}'

    # nome pasta
    pasta = './dataset/'

    # Verificar se a pasta existe
    if not os.path.exists(pasta):
        # Criar a pasta
        os.makedirs(pasta)
        print(f"A pasta '{pasta}' foi criada.")

    # Ajustando nome do arquivo para local de download (dataset)
    nome_arquivo = f'./dataset/{nome_arquivo}'

    # Realizando o download do arquivo
    download(url, nome_arquivo, quiet = False)

    return None

def preencher_matriz_contratos(arquivo: str):
    """
    Coletar as informações do arquivo baixado
    """
    # Ajustando nome do arquivo adicionando o local de download (dataset)
    nome_arquivo: str = f'./dataset/{arquivo}'

    # Abrindo o arquivo no modo de leitura
    with open(nome_arquivo, 'r') as arq:
        # Ler todas as linhas do arquivo em uma lista
        linhas = arq.readlines()

    # Verificando primeira linha
    if len(linhas[0].strip().split(' ')) < 4:
        # Remove primeira linha
        linhas = linhas[1:]
        
    # Verificando a quantidade de fornecedores
    qtd_fornecedores: int = 0
    qtd_mes_ini: int = 0
    qtd_mes_fim: int = 0
    print('2.1. Verificando a quantidade de fornecedores\n')
    for linha in linhas:
        item: list = linha.strip().split(' ')
        num_fornecedor: int = int(item[0])
        num_mes_ini: int = int(item[1])
        num_mes_fim: int = int(item[2])
        if qtd_fornecedores < num_fornecedor:
            qtd_fornecedores: int = num_fornecedor
        if qtd_mes_ini < num_mes_ini:
            qtd_mes_ini: int = num_mes_ini
        if qtd_mes_fim < num_mes_fim:
            qtd_mes_fim: int = num_mes_fim
 
    # Gerando a matriz utilizando a biblioteca Numpy com a quantidade ideal de fornecedores
    #matriz = np.full((qtd_fornecedores + 1, 4, 4), float('inf'))
    print('2.2. Gerando a matriz\n')
    matriz = np.full((qtd_fornecedores + 1, qtd_mes_ini + 1, qtd_mes_fim + 1), float('inf'))

    # Preenchendo os dados dos fornecedores
    print('2.3. Preenchendo os dados dos fornecedores\n')
    for linha in linhas:
        item: list = linha.strip().split(' ')
        fornecedor: int = int(item[0])
        inicio: int = int(item[1])
        fim: int = int(item[2])
        valor: float = float(item[3])
        matriz[fornecedor][inicio][fim] = valor

    return matriz     

def imprimir_matriz(matriz: any):
    """
    Imprimir o valor do contrato a partir das informações passadas pelo usuário.
    """
    ### Imprimir os resultados especificos para validacao da matriz de contratos
    # Iniciando Validador
    val: int = 0
    # informar dados
    while val == 0:
        fornecedor: int = int(input('Forneça o número do fornecedor ou 0 para apresentar a matriz completa: '))
        if fornecedor > len(matriz):
            print(f'Não há um fornecedor com o código informado, informe um codigo de fornecedor até {len(matriz)}!')
        else:
            val = 1
    if fornecedor == 0:
        #Retornando matriz completa
        return matriz
    else:
        # Zerando Validador
        val: int = 0
        # informar dados
        while val == 0:
            mes_ini: int = int(input('Forneça o número referente ao mes inicial: '))
            if fornecedor > len(matriz):
                print(f'Não há um mês com o código informado, informe um mês até {len(matriz[fornecedor])}!')
            else:
                val = 1

        # Zerando Validador
        val: int = 0
        # informar dados
        while val == 0:
            mes_fim: int = int(input('Forneça o número referente ao mes final: '))
            if fornecedor > len(matriz):
                print(f'Não há um mês com o código informado, informe um mês até {len(matriz[fornecedor])}!')
            else:
                val = 1

        vlr_contrato: float = matriz[fornecedor][mes_ini][mes_fim]

        return vlr_contrato

def exportar_csv(arquivo, matriz):

    # nome pasta
    pasta: str = './dataset'

    # Certifique-se de que a pasta existe
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    # Caminho completo do arquivo
    caminho_arquivo: str = f'{pasta}/{arquivo}'

    # Criando / abrindo o arquivo CSV
    with open(caminho_arquivo, 'w') as arq_csv:
        # Definindo contador inicial
        contador: int = 1
        # Adicionando a matriz no arquivo
        for bloco in matriz[1:]:
            csv.writer(arq_csv).writerow([f'Valores do fornecedor: {contador}'])
            csv.writer(arq_csv, delimiter=',').writerows(bloco)
            contador+=1
    
    print(f"O arquivo {arquivo} foi criado com sucesso na pasta {pasta}!")

    return None