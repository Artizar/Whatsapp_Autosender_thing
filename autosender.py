from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://web.whatsapp.com')

names,nama=['Rauf'],0
pesan = input("Masukan Pesan:")
confirmation = input("Is the message ready to be sent? (yes/no): ").lower()

if confirmation == 'yes':
    time.sleep(5)
    def sendwa():
        for nama in names:
            user = driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
            user.click()
            user.clear()
            user.send_keys(nama)
            user.send_keys(Keys.ENTER)
            time.sleep(5)

            msg = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            msg.click()
            msg.send_keys(pesan)
            user.send_keys(Keys.ENTER)
            time.sleep(10)
            Tombol = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            Tombol.click()
            time.sleep(10)

        driver.quit()
        print("Pesan telah terkirim")

    sendwa()

else:
    print("message is canceled")
    driver.quit()