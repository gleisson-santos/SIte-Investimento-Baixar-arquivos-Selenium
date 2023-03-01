# Selenium_baixar_aquivo
 Pequeno codigo em Selenium para acessar site, baixar o arquivo e tratar com o pandar. 
 
 
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

diretorio = r'C:\Users\gleisson.santos\Desktop\teste'

#Alterar o diretorio padrão de download
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": diretorio,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})


driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


driver.get("https://br.investing.com/currencies/usd-brl-historical-data")
time.sleep(5)
#Tratativa do Pup up
   
driver.find_element(By.CLASS_NAME, "download-data_text__1gHMw").click()
```


![image](https://user-images.githubusercontent.com/33934341/195913955-17a451c2-f1c8-48a2-9d09-699a16942071.png)




```python
#Importar e tratar arquivo/DataFrame
import os
import glob
import pandas as pd


path = r'C:\Users\gleisson.santos\Desktop\teste'
files = os.listdir(path)
df = pd.DataFrame()


files_csv = [path + '\\' + f for f in files if f[-3:] == 'csv']
for f in files_csv:
    data = pd.read_csv(f)
    df = df.append(data)
display(df)
```

![image](https://user-images.githubusercontent.com/33934341/195913980-ab62a6c0-f8cb-4e01-bdbf-f099a91dcedb.png)
