import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import pyautogui as pg
import mouse,time
'''Driver Setting :'''
driver_service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.get("https://www.skyscanner.co.il/")
driver.maximize_window()
''' Flight From : '''
class Travel_from():
    flight_from = driver.find_element(By.XPATH, "//*[@id='fsc-origin-search']")
    flight_from.click()
    # flight_from.clear()
    flight_from.send_keys('Tlv')
    time.sleep(1)
'''Flight To :'''
class Travel_to():
    flight_to = driver.find_element(By.CSS_SELECTOR,'#fsc-destination-search')
    flight_to.click()
    flight_to.send_keys('Portugal')
    time.sleep(1)
'''Date OF Departure: '''
class departure():
    Depart = driver.find_element(By.CSS_SELECTOR, '#depart-fsc-datepicker-button > span')
    Depart.click()
    time.sleep(2)
    Departdate=driver.find_element(By.XPATH,'//*[@id="depart-fsc-datepicker-popover"]/div/div/div[2]/div/table/tbody/tr[4]/td[2]/button/span')
    Departdate.click()
    Return=driver.find_element(By.XPATH,'//*[@id="return-fsc-datepicker-button"]/span')
    Return.click()
    time.sleep(2)
    Returndate= driver.find_element(By.XPATH,'//*[@id="return-fsc-datepicker-popover"]/div/div/div[2]/div/table/tbody/tr[5]/td[4]/button/span')
    Returndate.click()
while (True):
    mouse.move(1576,500, absolute=True,duration=3)
    mouse.click()
    break
time.sleep(1)
driver.quit()



