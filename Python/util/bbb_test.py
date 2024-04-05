import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pywinauto import Application

# Função para votar em um participante
def vote(participant_number):
    # Inicia o navegador Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Abre o site do BBB
    driver.get("https://gshow.globo.com/realities/bbb/")
    time.sleep(5)  # Aguarda o site carregar

    # Encontra o botão de votar e clica nele
    vote_button = driver.find_element_by_class_name("btnVote")
    vote_button.click()

    # Espera o site carregar o modal de votação
    time.sleep(5)

    # Simula interações com o teclado usando PyAutoGUI
    pyautogui.press('tab', presses=5, interval=0.5)
    pyautogui.press('enter')

    # Aguarda o modal de votação carregar completamente
    time.sleep(5)

    # Simula votação usando Pywinauto
    app = Application().connect(title_re="Votação BBB")
    dialog = app.window(title_re="Votação BBB")
    edit = dialog.Edit
    edit.type_keys(participant_number)
    pyautogui.press('enter')

    # Fecha o navegador
    driver.quit()

# Exemplo de uso: votar no participante 1
vote("1")