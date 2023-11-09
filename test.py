from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import auth_date


browser = webdriver.Chrome()

try:
    browser.get('https://eurotec.ua/admin/index.php?route=module/universal_import&user_token=YXWLtNhC4kidb4JwF18pdxCBhoXlUf6Z')
    time.sleep(1)
    username_input = browser.find_element(By.NAME, 'username')
    username_input.clear()
    username_input.send_keys(auth_date.username)
    time.sleep(1)
    password_input = browser.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(auth_date.password)
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(1)
    select_update = browser.find_element(By.NAME, 'import_type').click()
    time.sleep(1)
    confirm_select_update = browser.find_element(By.XPATH, '//*[@id="importStep1"]/div[2]/div[1]/select/option[2]').click()
    select_source = browser.find_element(By.NAME, 'import_source').click()
    time.sleep(1)
    confirm_source = browser.find_element(By.XPATH, '//*[@id="importStep1"]/div[3]/div[1]/select/option[2]').click()
    time.sleep(1)
    input_url = browser.find_element(By.NAME, 'import_file').send_keys('b2b.eurotec.ua/price/eurotec_update.csv')
    time.sleep(1)
    button_confirm_1 = browser.find_element(By.XPATH, '//*[@id="importStep1"]/div[6]/button').click()
    time.sleep(1)
    select_identifier = browser.find_element(By.NAME, 'item_identifier').click()
    time.sleep(1)
    confirm_identifier = browser.find_element(By.XPATH,'//*[@id="tab-setting-common"]/div[4]/div[1]/select/option[2]').click()
    time.sleep(1)
    button_confirm_2 = browser.find_element(By.XPATH, '//*[@id="importStep2"]/div[3]/button[2]').click()
    time.sleep(1)
    button_confirm_3 = browser.find_element(By.XPATH, '//*[@id="importStep3"]/div[4]/button[2]').click()
    time.sleep(1)
    button_confirm_5 = browser.find_element(By.XPATH, '//*[@id="importStep4"]/div[12]/button[3]').click()
    time.sleep(1)
    button_confirm_start = browser.find_element(By.XPATH, '//*[@id="importStep5"]/div[3]/button[1]').click()
    time.sleep(20)

    time.sleep(10)
except Exception as ex:
    print(ex)
    browser.close()
    browser.quit()