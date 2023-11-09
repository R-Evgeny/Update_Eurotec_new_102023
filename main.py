import pandas as pd
import datetime
import ftplib
import time
import auth_date
from auth_date import user_ftp, password_ftp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def mirs():

    file_path = "mirs.xlsx"

    df = pd.read_excel(file_path)
    df = df.rename(columns={
        "Unnamed: 1": "manufacturer",
        "Unnamed: 2": "sku",
        "Unnamed: 9": "quantity",
        "Unnamed: 10": "price"
    })
    df_blanco = df[["manufacturer", "sku", "quantity", "price"]]
    df_blanco = df_blanco[df_blanco["manufacturer"] == 'BLANCO']
    df_blanco = df_blanco.loc[9:]
    df_blanco['price'] = df_blanco['price'].astype('float')
    df_blanco.loc[:, 'price'] *= 0.9

    df_liebherr = df[["manufacturer", "sku", "quantity", "price"]]
    df_liebherr = df_liebherr[df_liebherr["manufacturer"] == 'Liebherr']
    df_liebherr = df_liebherr.loc[9:]

    df_falmec = df[["manufacturer", "sku", "quantity", "price"]]
    df_falmec = df_falmec[df_falmec["manufacturer"] == 'Falmec']
    df_falmec = df_falmec.loc[9:]

    df_vestel = df[["manufacturer", "sku", "quantity", "price"]]
    df_vestel = df_vestel[df_vestel["manufacturer"] == 'Vestel']
    df_vestel = df_vestel.loc[9:]

    df_nivona = df[["manufacturer", "sku", "quantity", "price"]]
    df_nivona = df_nivona[df_nivona["manufacturer"] == 'Nivona']
    df_nivona = df_nivona.loc[9:]

    global df_mirs
    df_mirs = pd.concat([df_blanco, df_liebherr, df_falmec, df_vestel, df_nivona], axis=0)

def bsh():
    global df_bsh
    file_path = "bsh.xls"
    df = pd.read_excel(file_path)
    df = df.rename(columns={
        "Unnamed: 1": "manufacturer",
        "Unnamed: 4": "sku",
        "Unnamed: 7": "quantity",
        "Unnamed: 6": "price"
    })
    df_bsh = df[["manufacturer", "sku", "quantity", "price"]]
    df_bsh = df_bsh.loc[11:]
    df_bsh["quantity"].replace({"да": "2", "нет": "0"}, inplace=True)

def franke():
    global df_franke
    file_path = "franke.xlsx"
    df = pd.read_excel(file_path)
    df = df.rename(columns={
        "FUN": "sku",
        "Доступно": "quantity"
    })
    df_franke = df[["sku", "quantity"]]
    df_franke = df_franke.loc[1:]
    df_franke["quantity"].replace({"наявність по запиту": "0"}, inplace=True)

def teka():
    global df_teka
    file_path = "teka.xlsx"
    df = pd.read_excel(file_path)
    df = df.rename(columns={
        "Unnamed: 0": "sku",
        "Unnamed: 2": "quantity"
    })
    df_teka = df[["sku", "quantity"]]
    df_teka = df_teka.loc[12:]
    df_teka["quantity"].replace({"> 10": "12"}, inplace=True)

def upload_to_ftp():
    # Подключение к FTP-серверу
    ftp = ftplib.FTP('eurotec.ua', user_ftp, password_ftp)

    # Переход в нужную папку
    ftp.cwd('/')

    # Открытие файла для чтения
    with open('eurotec_update.csv', 'rb') as f:
        # Загрузка файла на сервер
        ftp.storbinary('STOR eurotec_update.csv', f)

    # Закрытие соединения с FTP-сервером
    ftp.quit()

    print('Файл успешно загружен')

def update_eurotec_onsite():
    browser = webdriver.Chrome()

    try:
        browser.get(
            'https://eurotec.ua/admin/index.php?route=module/universal_import&user_token=YXWLtNhC4kidb4JwF18pdxCBhoXlUf6Z')
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
        confirm_select_update = browser.find_element(By.XPATH,
                                                     '//*[@id="importStep1"]/div[2]/div[1]/select/option[2]').click()
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
        confirm_identifier = browser.find_element(By.XPATH,
                                                  '//*[@id="tab-setting-common"]/div[4]/div[1]/select/option[2]').click()
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

def blanco():
    file_path = "mirs.xlsx"

    df = pd.read_excel(file_path)
    df.insert(1, "В наявності?", 1)
    df = df.rename(columns={
        "Unnamed: 2": "Артикул",
        "Unnamed: 9": "Запаси",
        "Unnamed: 10": "Звичайна ціна",
        "Unnamed: 1": "manufacture"
    })
    df_blanco = df[["Артикул", "В наявності?", "Запаси", "Звичайна ціна", "manufacture"]]
    df_blanco = df_blanco[df_blanco["manufacture"] == 'BLANCO']
    df_blanco = df_blanco.loc[9:]

    df_blanco.to_csv("blanco_update.csv")

def update_blanco_onsite():
    browser = webdriver.Chrome()

    try:
        browser.get('https://blanco-ukraine.com.ua/wp-admin/edit.php?post_type=product&page=product_importer#/')
        time.sleep(1)
        username_input = browser.find_element(By.ID, 'user_login')
        username_input.clear()
        username_input.send_keys(auth_date.username_blanco)
        time.sleep(1)
        password_input = browser.find_element(By.ID, 'user_pass')
        password_input.clear()
        password_input.send_keys(auth_date.password_blanco)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)
        time.sleep(1)
        file000_input = browser.find_element(By.XPATH,
                                             '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[3]/form/section/table/tbody/tr[1]/td/input[1]').send_keys(
            r'C:\Python\Update_Eurotec\blanco_000.csv')
        time.sleep(3)
        checkbox_update000 = browser.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[3]/form/section/table/tbody/tr[2]/td/input[2]').click()
        time.sleep(1)
        submit_file000_input = browser.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[3]/form/div/button').click()
        time.sleep(5)
        submit_file000 = browser.find_element(By.XPATH,
                                              '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[3]/form/div/button').click()
        time.sleep(60)
        browser.get('https://blanco-ukraine.com.ua/wp-admin/edit.php?post_type=product&page=product_importer#/')
        time.sleep(2)
        file000_input = browser.find_element(By.XPATH,
                                             '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[3]/form/section/table/tbody/tr[1]/td/input[1]').send_keys(
            r'C:\Python\Update_Eurotec\blanco_update.csv')
        time.sleep(3)
        checkbox_update000 = browser.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[3]/form/section/table/tbody/tr[2]/td/input[2]').click()
        time.sleep(1)
        submit_file000_input = browser.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[3]/form/div/button').click()
        time.sleep(5)
        submit_file000 = browser.find_element(By.XPATH,
                                              '/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/div[3]/form/div/button').click()
        time.sleep(60)

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

def start():
    starttime = datetime.datetime.now()

    mirs()
    bsh()
    franke()
    teka()

    df = pd.concat([df_mirs, df_bsh, df_franke, df_teka], axis=0)
    df = df.reset_index(drop=True)
    df.to_csv("eurotec_update.csv")

    upload_to_ftp()

    update_eurotec_onsite()
    print('EuroTec - OK')
    update_blanco_onsite()
    print('Blanco - OK')

    diftime = datetime.datetime.now() - starttime
    print(diftime)

def main():
    start()

if __name__ == '__main__':
    main()