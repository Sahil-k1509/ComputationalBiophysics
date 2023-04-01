import requests
from bs4 import BeautifulSoup
from selenium import webdriver

OUTPUT_FILE_NAME = 'MHC_paratope_new.txt'

path_to_chromedriver = '/Users/91819/Desktop/chromedriver'
url = 'http://www.imgt.org/3Dstructure-DB/'

driver = webdriver.Chrome(executable_path=path_to_chromedriver)
driver.implicitly_wait(5)
driver.get(url)
driver.find_element('xpath', '//*[@id="species"]/option[28]').click()
driver.find_element('xpath', '//*[@id="radio_pMH1"]').click()            # choose pMHCI   (input)
driver.find_element('xpath', '//*[@id="datas"]/p[2]/input[1]').click()   # click submit    (button)

page = driver.page_source.encode('utf-8')
soup = BeautifulSoup(page, 'html.parser')
rows = soup.select('body#result div#data table.Results tbody tr')[1:]

with open(OUTPUT_FILE_NAME, 'w') as file:
    indx = 0
    for row in rows:
        indx += 1
        mhc = row.select('td')[2].text
        url_suffix = row.select('td')[1].find('a').text.upper()
        url_next = 'http://www.imgt.org/3Dstructure-DB/cgi/details.cgi?pdbcode=' + url_suffix + '&Part=Epitope'
        
        content = requests.get(url_next).content
        soup2 = BeautifulSoup(content, 'html.parser')
        paratope = ''
        table = soup2.select('body#result div#mybody div#main table')[0]
        for i in table.select('tr')[2].select('td')[1].select('span a'):
            aa = i.text
            paratope += aa
        outputstr = f'{mhc}, {url_suffix}, {paratope}\n'
        file.write(outputstr)
        
