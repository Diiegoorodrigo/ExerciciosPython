# Crie uma tupla com os times da Tabela do campeonato Brasileiro
# mostre os 5 primeiros colocados
# mostra o Z4
# Coloque a tabela em ordem alfabética
# Mostre em que posição o Vasco está
tabela = ('Flamengo', 'Bahia', 'Botafogo', 'Palmeiras', 'Cruzeiro', 'Athletico-PR', 'São Paulo', 'Bragantino', 'Internacional', 'Atlético-MG', 'Fortaleza', 'Juventude', 'Criciúma', 'Cuiabá', 'Vitória', 'Vasco da Gama', 'Atlético-GO', 'Corinthians', 'Grêmio', 'Fluminense')
print(f'Os cinco primeirs colocados são {tabela[0:5]}')
print('==='*30)
print(f'Os quatro últimos colocados são {tabela[16:]}')
print('==='*30)
print(f'A tabela em ordem alfabética fica assim: {sorted(tabela)}')
print('==='*30)
p = (tabela.index('Vasco da Gama') + 1)
print(f'O Vasco está em {p}º Colocado')