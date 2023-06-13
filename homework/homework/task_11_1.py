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
    print('открыли браузер на странице ' + link)
    assert driver.current_url == link, 'Неверный url сайта'
    print(driver.title)
    assert driver.title == driver_title, 'неверный заголовок на сайте'
    time.sleep(3)
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item',)
    time.sleep(1)
    print(('Название кнопки: ' + tabs[1].text))
    assert tabs[1].text == 'Контакты'

    contacts_button = tabs[1]
    assert contacts_button.is_displayed() == True, 'Кнопка контактов не видна на странице'
    contacts_button.click()
    print('Нажали кнопку контакты и перешли в раздел Контактов')
    time.sleep(3)

    """Ищем лого "Тензор"""

    logo_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    print(logo_tensor)
    assert logo_tensor.is_displayed() == True, 'логотип Тензора не виден на странице'
    logo_tensor.click()
    time.sleep(3)

    """Переходим на другую вкладку"""
    print(driver.window_handles)
    # driver.switch_to_window(driver.window_handles[1])  # переходим на 2ую вкладку
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    """Ищем элемент Контакты"""
    power_in_peoples_blok = driver.find_elements(By.XPATH, "//*[@id='container']/div[1]/div/div[5]/div/div/div[1]/div/p[1]")  # находим блок сила в людях по XPath
    print(type(power_in_peoples_blok))
    print(power_in_peoples_blok[0].text)
    assert power_in_peoples_blok[0].text == 'Сила в людях', "Текст в блоке СИЛА В ЛЮДЯХ неверный"

    """Переходим по кнопке ПОДРОБНЕЕ в блоке СИЛА В ЛЮДЯХ"""
    podrobnee_button_text = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__card-text [href='/about']")

    print(podrobnee_button_text.text)
    assert podrobnee_button_text.text == "Подробнее"
    print("Элемент подробнее на экране:" + str(podrobnee_button_text.is_displayed()))
    assert podrobnee_button_text.is_displayed() == True
    podrobnee_button_text.location_once_scrolled_into_view


    action_chains = ActionChains(driver)
    action_chains.move_to_element(podrobnee_button_text)
    action_chains.double_click(podrobnee_button_text)

    action_chains.perform()
    time.sleep(3)

    print(driver.current_url)

    assert driver.current_url == link_about, "Перешли на неверную страницу"

    print('Тест пройден')



finally:
    driver.quit()