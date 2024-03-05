# O presente projeto foi construído como parte da aula 1 sobre automação do treinamento da HashTag treinamentos

# Objetivo do projeto: Construir um script para automatizar a tarefa de cadastrar itens em um banco de dados

# Primeiro, vamos importar as bibliotecas necessárias
import pyautogui
import time

# Comandos básicos da biblioteca 'pyautogui' utilizada para a automatização
# pyautogui.write -> escrever um texto especificado
# pyautogui.press -> apertar uma tecla especificada
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# Funções importantes
## pyautogui.PAUSE = 0.3 -> Utilizado para pausar a execução do script por período de tempo especificado

# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa 
## Site: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 0.3

## Primeiro, devemos abrir o navegador para buscar pelo site no qual cadastraremos os itens 
### abrir o navegador (chrome)
pyautogui.press("win") # -> Indicar ao computador para abrir a "barra de pesquisa do windows"
pyautogui.write("chrome") # -> Indicar ao computador para pesquisar pelo Google chrome na "barra de pesquisa do windows"
pyautogui.press("enter") # -> Indicar ao computador para dar "enter", abrindo assim o navegador



## entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # -> Indicar ao computador para abrir digitar o link especificado na barra de busca do Chrome
pyautogui.press("enter") # -> Indicar ao computador para dar "enter"
time.sleep(3) # -> Indicar ao computador para dar uma pausa no script, aguardando assim a página da web carregar


# Passo 2: Fazer login
## selecionar o campo de email
pyautogui.click(x=774, y=514) # -> Indicar ao computador aonde clicar, com base na posição capturada por outro programa em Python

## escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com") # -> Indicar ao computador o que deve ser escrito no campo de e-mail para fazer login
pyautogui.press("tab") # -> Indicar ao computador que ele deve passar para o próximo campo, para preenchermos a próxima informação
pyautogui.write("sua senha") # -> Indicar ao computador qual senha deve ser escrita
pyautogui.click(x=937, y=718) # -> Indicar ao computador para clicar no botão de login
time.sleep(3) # -> Pausar o script por um tempo pré-estabelecido para dar tempo de a página carregar

# Passo 3: Importar a base de produtos para serem cadastradas no banco de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv") # Tabela com os produtos e suas informações a serem cadastradas no banco de dados

print(tabela)

# Passo 4: Cadastrar um produto

## Utilizamos um laço de repetição para captar as informações da tabela e elas serem preenchidas automaticamente no site

for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=777, y=364)
    # pegar da tabela o valor do campo que a gente quer preencher
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
