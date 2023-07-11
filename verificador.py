def verificar_linhas_em_branco(arquivo_txt):
    with open(arquivo_txt, 'r') as arquivo:
        linhas = arquivo.readlines()
        for indice, linha in enumerate(linhas, start=1):
            if linha.strip() == '':
                print(f'Linha em branco encontrada na linha {indice}')

# Exemplo de uso
arquivo_txt = 'C:\\Users\\diego.marques\\Desktop\\Teste'
verificar_linhas_em_branco(arquivo_txt)
