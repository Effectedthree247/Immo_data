from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller as chromedriver

chromedriver.install()
page=1
counter = 2

driver = webdriver.Chrome()
driver.get(f"https://www.zimmo.be/nl/panden/?status=1&hash=08da334dc71b4ff067486a87c019adff&priceIncludeUnknown=1&priceChangedOnly=0&bedroomsIncludeUnknown=1&bathroomsIncludeUnknown=1&constructionIncludeUnknown=1&livingAreaIncludeUnknown=1&landAreaIncludeUnknown=1&commercialAreaIncludeUnknown=1&yearOfConstructionIncludeUnknown=1&epcIncludeUnknown=1&queryCondition=and&includeNoPhotos=1&includeNoAddress=1&onlyRecent=0&onlyRecentlyUpdated=0&isPlus=0&excludedEstates%5B0%5D=JW8WO&excludedEstates%5B1%5D=JZPPQ&excludedEstates%5B2%5D=JZHQD&excludedEstates%5B3%5D=K00P0&notarySale=0&region=list&district=MzAYLMAQAA%253D%253D&pagina={page}#gallery")
button = driver.find_element(By.ID, "didomi-notice-agree-button")
button.click()

links_list = []
price_list = []
addresses = []

pages = driver.find_elements(By.CSS_SELECTOR, "#wrapper > div.content > div.container.properties-list-container.fade.properties-list-gallery.in > div.property-results > div.list-options.bottom > div.pagination-container.clearfix > ul > li > a")
while counter < len(pages) -1:
    pages = driver.find_elements(By.CSS_SELECTOR,
                                 "#wrapper > div.content > div.container.properties-list-container.fade.properties-list-gallery.in > div.property-results > div.list-options.bottom > div.pagination-container.clearfix > ul > li > a")
    links = driver.find_elements(By.CSS_SELECTOR,"#wrapper > div.content > div.container.properties-list-container.fade.properties-list-gallery.in > div.property-results > div.property-results_container > div.property-item")
    time.sleep(1)
    for link in links:
        tag = link.find_element(By.CLASS_NAME,"property-item_link")
        links_list.append(tag.get_attribute("href"))

        price = link.find_element(By.CLASS_NAME, "property-item_price")
        price_list.append(price.text)

        address = link.find_element(By.CLASS_NAME, "property-item_address")
        new_address = address.text.replace("\n", " , ")
        addresses.append(new_address)
    current_page = pages[counter]
    current_page.click()
    counter += 1

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc3B6Dqjg6W0WNr9rWRClCRLA0ayfzBDFqXF3WCoapqZaN0GA/viewform?usp=sf_link")
for n in range(len(price_list)):
    address_input = driver.find_element(By.CSS_SELECTOR,
                                        "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    price_input = driver.find_element(By.CSS_SELECTOR,
                                      "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    link_input = driver.find_element(By.CSS_SELECTOR,
                                     "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    button = driver.find_element(By.CSS_SELECTOR,
                                 "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div")
    address_input.send_keys(addresses[n])
    price_input.send_keys(price_list[n])
    link_input.send_keys(links_list[n])
    button.click()
    next = driver.find_element(By.CSS_SELECTOR,
                               "body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a")
    next.click()
