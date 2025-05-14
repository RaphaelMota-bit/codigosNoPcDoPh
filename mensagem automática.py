import schedule
import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def executar_script():
    # Diretório base
    base_dir = os.getcwd()

    # Caminhos relativos convertidos para absolutos
    caminho_perfil = os.path.join(base_dir, "perfil_selenium")
    caminho_driver = os.path.join(base_dir, "chromedriver-win64", "chromedriver-win64", "chromedriver.exe")


    # Configuração do ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument(rf"--user-data-dir={caminho_perfil}")
    service = Service(caminho_driver)
    driver = webdriver.Chrome(service=service, options=options)

    # Abre o WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()

    # Espera até que o WhatsApp Web carregue completamente
    wait = WebDriverWait(driver, 90)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))

    def enviar_mensagem(contato, mensagens):
        try:
            search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))
            search_box.clear()
            search_box.send_keys(contato)
            time.sleep(random.uniform(2, 5))
            search_box.send_keys(Keys.ENTER)
            time.sleep(random.uniform(3, 6))

            chat_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")))

            for mensagem in mensagens:
                chat_box.send_keys(mensagem)
                time.sleep(random.uniform(1, 2))
                chat_box.send_keys(Keys.ENTER)
                time.sleep(random.uniform(1, 2))

            print(f"✅ Mensagens enviadas para {contato}")

        except Exception as e:
            print(f"❌ Erro ao enviar mensagem para {contato}: {e}")

    def enviar_mensagens_agendadas():
        # contatos = ["xd", "Mano Kuririn", "Rafael Ferreira", "Elias", "Henrique Qi Qi", "micro SD ⚜️", "π8" , "Sophia" , "Neithan love of my life ❤️" , "Litlle Ruan" , "grazi" , "luiza Qi" , "amor ❤️"]
        contatos = ["xd"]
        mensagens = [
            "hey hey",
            "Quer lanchar oq amanhã?",
        ]

        for contato in contatos:
            enviar_mensagem(contato, mensagens)
            tempo_espera = random.uniform(10, 30)
            print(f"⏳ Aguardando {tempo_espera:.2f} segundos antes de enviar para o próximo contato...")
            time.sleep(tempo_espera)

    enviar_mensagens_agendadas()
    driver.quit()

# Agendamento
schedule.every().day.at("20:00").do(executar_script)

# Execução imediata para teste
executar_script()
