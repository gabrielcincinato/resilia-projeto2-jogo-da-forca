# Lista de palavras
with open('palavras.txt', 'r', encoding='utf-8') as file:
    lista_palavras = file.read().replace(' ', '').replace('\n', '').split(',')

with open('logo.txt', 'r', encoding='utf-8') as file:
    logo = file.readlines()
