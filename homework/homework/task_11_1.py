# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


"""Данные для входа"""
driver = webdriver.Chrome()  #executable_path='C:\\Python\\Python311\\chromedriver.exe')
driver.maximize_window()
link = 'https://sbis.ru/'
time.sleep(2)
driver_title ='СБИС — экосистема для бизнеса: учет, управление и коммуникации'
link_about = 'https://tensor.ru/about'

"""Переход на сайт"""
try:

    driver.get(link)
    assert driver.current_url == link, 'Неверный url сайта'
    assert driver.title == driver_title, 'неверный заголовок на сайте'
    time.sleep(3)
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item',)
    time.sleep(1)
    assert tabs[1].text == 'Контакты'

    contacts_button = tabs[1]
    contacts_button.click()
    time.sleep(3)

    """Ищем лого "Тензор"""

    logo_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    assert logo_tensor.is_displayed() == True, 'логотип Тензора не виден на странице'
    logo_tensor.click()
    time.sleep(3)

    """Переходим на другую вкладку"""
    # driver.switch_to_window(driver.window_handles[1])  # переходим на 2ую вкладку
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    """Ищем элемент Контакты"""
    power_in_peoples_blok = driver.find_elements(By.XPATH, '//p[text()="Сила в людях"]')  # находим блок сила в людях по XPath
    assert power_in_peoples_blok[0].text == 'Сила в людях', "Текст в блоке СИЛА В ЛЮДЯХ неверный"

    """Переходим по кнопке ПОДРОБНЕЕ в блоке СИЛА В ЛЮДЯХ"""
    podrobnee_button_text = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__card-text [href='/about']")

    assert podrobnee_button_text.text == "Подробнее"
    assert podrobnee_button_text.is_displayed() == True
    podrobnee_button_text.location_once_scrolled_into_view
    link_about = driver.find_element(By.CSS_SELECTOR, '[href="/about"][class="tensor_ru-Header__menu-link"]')
    link_about.click()
    time.sleep(3)
    about_page = driver.current_url
    assert about_page == link_about

    time.sleep(3)

    print('Тест пройден')

finally:
    driver.quit()