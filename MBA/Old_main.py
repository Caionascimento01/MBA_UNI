from Lib import download_dataset
from Lib import preencher_matriz_contratos
from Lib import imprimir_matriz
from Lib import exportar_csv

def main():
    
    ### Download do dataset
    # link simulacao 1
    #link_arq: str = "https://drive.google.com/file/d/1YjPaHv8aAVsXNzhHxum5gyUDFfY5iw1_/view?usp=drive_link"
    # link simulacao 2
    #link_arq: str = "https://drive.google.com/file/d/1uAjzXIO7ST4qMED12dtJi3D2_vlu84Rk/view?usp=drive_link"
    # link simulacao 3
    link_arq: str = "https://drive.google.com/file/d/1XqF3GOrqvHpLtNUSDXZivFn2KtSPdihL/view?usp=drive_link"
    arq_txt: str = 'entradagrande.txt'
    print('1. Baixando o arquivo\n')
    download_dataset(link_arq,arq_txt)

    ### Preencher a matriz de contratos
    print('2. Gerando a matriz\n')
    contratos = preencher_matriz_contratos(arq_txt)

    # Realizar verificação na matriz
    print('3. imprimindo valores\n')
    valor_matriz: float = imprimir_matriz(contratos)
    print(f'\nO valor do contrato é R$ {valor_matriz}')

    ### Exportar a matriz de contratos
    arq_contratos = "contratosgrande.csv"
    print("\n")
    print('4. Exportando matriz em um arquivo CSV\n')
    exportar_csv(arq_contratos, contratos)
    
if __name__ == "__main__":
    main()