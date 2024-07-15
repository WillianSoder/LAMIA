from bs4 import BeautifulSoup
import numpy as np
import requests
import time


# Faz uma requisição à URL e obtém o conteúdo da página em formato de texto
html= requests.get('https://lista.mercadolivre.com.br/porsche-911-turbo#D[A:porsche%20911%20turbo]').text
soup = BeautifulSoup(html, 'lxml') # Analisa o HTML da página usando BeautifulSoup e o parser 'lxml'

anuncios = soup.find_all('li', class_ = 'ui-search-layout__item') # pgando a lista de anuncios 
precos_SP = [] # cria uma lista de preços vazia paar SP
precos_SC = [] # cria uma lista de prços vazia para SC

ano_user = int(input('Digite a partir de ano deseja buscar o carro: '))
if ano_user > 2024: # garantindo que o valor não seja maior que o ano atual
    ano_user = 2024
    
print('\nBucando anuncios...')
print('Anuncios encontrados e filtrados: \n')

for anuncio in anuncios: # percorrendo os anuncios 
    
    nome = anuncio.find('h2', class_ = 'ui-search-item__title').text # pegando o nome para filtrar os modelos
    if 'Turbo S' in nome:
        
        ano = int(anuncio.find('li', class_ = 'ui-search-card-attributes__attribute').text) # convertendo para ano para filtrar os carros com ano maior que o o valor definido pelo usuario 
        
        if ano >= ano_user: # filtrando a partir do ano desejado pelo usuario
            
            preco = int(anuncio.find('span', class_ = 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript').text.replace('R$','').replace('.','')) # pegando o preço tirando o 'R$' e os '.' e trtanformando em int
            localizacao = anuncio.find('span', class_ = 'ui-search-item__group__element ui-search-item__location').text # pegando o estado para realizar a filtragem 
            print(f"Nome: {nome}\nAno: {ano}\nPreço: {preco}\nLocalizção: {localizacao}\n\n")
            
            if 'São Paulo' in localizacao:
                precos_SP.append(preco)
            elif 'Santa Catarina' in localizacao:
                precos_SC.append(preco)
                
# usando os dados para calcular as estatisticas em SP
media_SP = np.mean(precos_SP)
mediana_SP = np.median(precos_SP)
MAX_SP = max(precos_SP)
MIN_SP = min(precos_SP)

# usando os dados para calcular as estatisticas em SC
media_SC = np.mean(precos_SC)
mediana_SC = np.median(precos_SC)
MAX_SC = max(precos_SC)
MIN_SC = min(precos_SC)

#exibindo resultados
print('\n\n')
print(f"A media de preço para 'Porsche 911 Turbo s em SP: {media_SP}R$\nA mediana de preço para 'Porsche 911 Turbo s em SP: {mediana_SP}\nO maior preço em SP: {MAX_SP}\nO menor preço em SP: {MIN_SP}")
print('\n\n')
print(f"A media de preço para 'Porsche 911 Turbo s em SC: {media_SC}R$\nA mediana de preço para 'Porsche 911 Turbo s em SC: {mediana_SC}\nO maior preço em SC: {MAX_SC}\nO menor preço em SC: {MIN_SC}")