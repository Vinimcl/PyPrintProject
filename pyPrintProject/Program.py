import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import os

def take_screenshots():

webdriver_path = 'C:\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe'

# Diretório que salva os prints
screenshot_folder = 'C:\\Imagens Domicilio\\'

if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Adiciona certificado digital
cert_path = 'C:\\Users\\Zapping010\\Certificados\\HERMES E CPF.pfx'  # Substitua pelo caminho do seu certificado
cert_password = '5012'

# URLs dos sites
urls = [
    'https://domicilio-eletronico.pdpj.jus.br/comunicacoes;tipo=Comunicacao'
]

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Carrega o certificado digital
options.add_argument(f'--ssl-key-store-type=pkcs12')
options.add_argument(f'--ssl-key-store={cert_path}')
options.add_argument(f'--ssl-key-store-password={cert_password}')

service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    for idx, url in enumerate(urls):
        driver.get(url)
        time.sleep(5)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_folder, f'screenshot_{idx + 1}_{timestamp}.png')
        driver.save_screenshot(screenshot_path)
        print(f'Screenshot de {url} salvo em: {screenshot_path}')

finally:
    driver.quit()

schedule.every().day.at("10:00").do(take_screenshots)

while True:
    schedule.run_pending()
    time.sleep(1)