import pyautogui
import time
 
 
pyautogui.PAUSE = 0.3
#abrir o google
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("Enter")
#entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")
time.sleep(3)

#Passo 2 fazer login
#selecionar o campo de email
pyautogui.click(x=882,y=418)
#escrever o email
pyautogui.write("eu.luiseduardo.pro@gmail.com")
pyautogui.press("Tab")
#escrever a senha
pyautogui.write("sua senha")
#botao login
pyautogui.click(x=972,y=573)
time.sleep(3)

#passo 3 importar a base de produtos
import pandas
#uma variavel pra receber a tabela
tabela = pandas.read_csv("produtos.csv") #ler o csv
#imprimir a tabela 
print(tabela) 

time.sleep(2)
#Passo 4, cadrastar um produto


for linha in tabela.index:
    #clicar no campo
    pyautogui.click(x=810,y=295)
    #pegar da tabela o valor do campo para preencher
    codigo=tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    #proximo campo
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    obs=tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("Tab")
    pyautogui.press("Enter") #cadrastar produto(enviar)
    #dar scroll
    pyautogui.scroll(5000)
    #passo 5 Repetir o passo 4 até o fim