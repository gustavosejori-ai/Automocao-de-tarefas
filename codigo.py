import time
import pyautogui
import pandas as pd
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "gustavosejori@gmail.com"
senha = "gustavo18"

#Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Entrar no site para testes
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

#Importando a base de produtos para o cadastro
tabela = pd.read_csv("produtos.csv")

#Fazer login colocando e-mail e senha
pyautogui.click(x=1645, y=375)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")  
pyautogui.press("enter")
time.sleep(5)

#Cadastrar o produto
for linha in tabela.index:
    pyautogui.click(x=1477, y=261)
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(5000)