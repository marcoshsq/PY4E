from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://google.com/recaptcha/api2/demo"
navegador.get(link)

chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')
navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
