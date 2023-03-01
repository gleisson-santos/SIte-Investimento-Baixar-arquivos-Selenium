from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()

driver.get("https://br.investing.com/currencies/usd-brl-historical-data")
time.sleep(2)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i').click()

driver.find_element(By.CLASS_NAME, "downloadBlueIcon ").click()

driver.find_element(By.ID, "loginFormUser_email").send_keys('jsgleisson@gmail.com')
driver.find_element(By.ID, "loginForm_password").send_keys('Design20*')

elementos = driver.find_elements_by_css_selector("a.orange")
elementos[2].click()
time.sleep(50)
driver.find_element(By.CLASS_NAME, "downloadBlueIcon ").click()