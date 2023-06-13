# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
"""
Тест №1
1 Перейти на https://sbis.ru/
2 Перейти в раздел "Контакты"
3 Найти баннер Тензор, кликнуть по нему
4 Перейти на https://tensor.ru/
5 Проверить, что есть блок новости "Сила в людях"
6 Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
"""
try:
    driver.get('https://sbis.ru/')
    contact = driver.find_element(By.CSS_SELECTOR, "[href='/contacts']")
    contact.click()
    sleep(2)
    banner = driver.find_element(By.CSS_SELECTOR, "[href='https://tensor.ru/']")
    banner.click()
    driver.switch_to.window(driver.window_handles[1])
    new = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-Index__card-title")
    driver.execute_script("return arguments[0].scrollIntoView(true);", new)
    sleep(2)
    assert new.text == 'Сила в людях', 'Не соответствует текст новости'
    about = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content [href='/about']")
    sleep(1)
    about.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Не верно открыт сайт'
    sleep(2)
    print('Тест №1 пройден!')
finally:
    driver.quit()
