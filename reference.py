
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import os
import argparse

def downloadPDFs(link, path = "C:\\Users\\PC\\Downloads\\"):

    options = webdriver.ChromeOptions()

    profile = {"plugins.always_open_pdf_externally": True,
                "download.default_directory" : path}
    options.add_experimental_option("prefs", profile)

    link = 'https://www.aldo.com.br/loja/produto/138527-1/gerador-de-energia-solar-growatt-solo-romagnole-aldo-solar-on-grid-gf-1484kwp-jinko-bifacial-tiger-pro-530w-min-10kw-3mppt-mono-220v'

    names = []

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(link)
    wait = WebDriverWait(driver, 15)
    folhetos = driver.find_element(By.CLASS_NAME, "folhetos")
    links = folhetos.find_elements(By.TAG_NAME, 'li')
    for link in links:
        pdf = link.find_element(By.TAG_NAME, 'a')
        href = pdf.get_property('href')

        name_original= href[href.rindex('/')+1:]
        name_new = pdf.get_attribute('title').lstrip(' ')
        names.append((name_original, name_new))

        driver.get(href)
        wait = WebDriverWait(driver, 15)

    time.sleep(10)
    driver.close()

    for name in names:
        path_old = path + name[0]
        path_new = path + name[1] + '.pdf'
        try:
            os.rename(path_old, path_new)
        except FileExistsError:
            os.rename(path_old, path_new[:-4] + '(1).pdf')
    
    print ('Downloads realizados com sucesso')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download de todos PDFs do kit da Aldo')
    parser.add_argument('link', type=str, help='Link do kit da Aldo')
    parser.add_argument('-p', '--path', type=str, action='store')
    args = parser.parse_args()

    if args.path:
        downloadPDFs(args.link, args.path)
    else:
        downloadPDFs(args.link)
