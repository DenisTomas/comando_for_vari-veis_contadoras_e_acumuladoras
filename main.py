import numpy as np

# Dados de referência
dados = [[20, 19.5], [20, 19.71], [20, 20.2], [20, 20.11],
         [21, 19.91], [21, 20.7], [21, 21.21], [21, 21.5],
         [25, 25.51], [25, 24.71], [25, 25.2], [25, 24.11]]

# Dicionário para armazenar os valores de referência e seus respectivos PVs
dados_por_preferencia = {}

# Agrupando os dados por valor de refernência
for dado in dados:
    sp, pv = dado
    if sp in dados_por_preferencia:
        dados_por_preferencia[sp].append(pv)
    else:
        dados_por_preferencia[sp] = [pv]

# Calculando média e desvio padrão para cada valor de referência
for sp, pvs in dados_por_preferencia.items():
    media = np.mean(pvs)
    desvio_padrao = np.std(pvs)
    print(f'Valor de referência: {sp}')
    print(f'Média: {media:.2f}')
    print(f'Desvio padrão: {desvio_padrao: .2f}')
    print()