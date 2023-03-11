# Create a tuple with the first 20 teams places in the Brazilian Football Championship in order. Then show:
# a) The first five teams b) The last 4 teams c) An alphabetical list of the teams d) What position Chapecoense is.

teams = ('Palmeiras', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG','Fluminense', 'Botafogo', 'Santos',
         'São Paulo', 'Bragantino', 'Avaí', 'Atlético-GO', 'Ceará SC', 'Flamengo', 'América-MG', 'Coritiba', 'Goiás',
         'Cuiabá', 'Fortaleza', 'Juventude')

print(f'Os cinco primeiros times são: {teams[:5]}')
print(f'Os últimos cinco times são: {teams[-5:]}')
print(f'Lista por ordem alfabética: {sorted(teams)}')

position = 1

for team in teams:
    if 'Chapecoense' in team:
        if team == 'Chapecoense':
            print(f'A Chapecoense está na {position}ª posição.')
        else:
            position += 1
    else:
        print('A Chapecoense não está na lista.')
        break
