from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime

# Caminho ChromeDriver
webdriver_path = 'C:\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe'

# Caminho certificado digital
user_data_dir = r'C:\HERMES E CPF.pfx'

# URL do site
url = 'https://domicilio-eletronico.pdpj.jus.br/comunicacoes;tipo=Comunicacao'
url = 'https://open.spotify.com/'
url = 'https://www.zappingcontadores.com.br/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Para executar em modo headless (sem interface gráfica)

service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(url)

    time.sleep(5)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = f'screenshot_{timestamp}.png'
    driver.save_screenshot(screenshot_path)
    print(f'Screenshot salvo em: {screenshot_path}')

finally:
    driver.quit()
