from selenium import webdriver
import bs4
from time import sleep

def parser() -> dict:
    driver = webdriver.Chrome()
    driver.get('https://coinmarketcap.com/')
    driver.maximize_window()
    px = 0
    for i in range(10):
        px += 1000
        driver.execute_script(f'window.scrollTo(0, {px})')
        sleep(0.1)

    html = driver.page_source
    driver.close()
    soup = bs4.BeautifulSoup(html, 'html.parser')

print(parser())

