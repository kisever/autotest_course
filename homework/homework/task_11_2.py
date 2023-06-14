# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


browser = webdriver.Chrome()
user_login, user_password = 'Perun_404', 'Perun_404'
name = "Питерский Петр"
message = "Привет"

try:
    browser.get("https://fix-online.sbis.ru/")
    browser.maximize_window()
    sleep(3)
    login = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[name="Login"]'))
    )
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)

    contacts = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="Контакты"]'))
    )
    contacts.click()
    sleep(5)
    contacts = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".NavigationPanels-SubMenu__headTitle"))
    )
    contacts.click()
    sleep(5)
    cr_message = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-RoundPlus"))
    )
    cr_message.click()
    sleep(5)
    search = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".controls-StackTemplate__top-area-content input"))
    )
    search.send_keys(name)

    person = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f".msg-addressee-item [title='{name}']"))
    )
    person.click()

    msg_text = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[role='textbox']"))
    )
    msg_text.send_keys(message)

    send_btn = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-BtArrow"))
    )
    send_btn.click()
    sleep(1)

    messages = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.msg-dialogs-item p'))
    )
    assert messages[0].text == message, "Отправленного сообщения нет в реестре"

    chain = ActionChains(browser)
    chain.move_to_element(messages[0])
    chain.perform()

    delete = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".controls-icon_style-danger"))
    )
    delete.click()

    sleep(3)
    assert browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')[0].text != message, 'Сообщение не было удалено'
    sleep(2)

finally:
    browser.quit()