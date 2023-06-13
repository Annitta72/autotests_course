# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
"""
Тест №2
1 Авторизоваться на сайте https://fix-online.sbis.ru/
2 Перейти в реестр Контакты
3 Отправить сообщение самому себе
4 Убедиться, что сообщение появилось в реестре
5 Удалить это сообщение и убедиться, что удалили
"""
try:
    driver.get('https://fix-online.sbis.ru/')
    sleep(1)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('Игра', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('Игра123', Keys.ENTER)
    sleep(5)
    contact = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"] [data-qa="NavigationPanels-Accordion__title"]')
    contact.click()
    sleep(2)
    contact = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contact.click()
    sleep(1)
    plus = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    plus.click()
    sleep(2)
    poisk = '.controls-StackTemplate__top-area-content .controls-Search__nativeField_caretEmpty'
    name = driver.find_element(By.CSS_SELECTOR, poisk)
    name.send_keys('Игрова Аня')
    sleep(1)
    my_name = driver.find_element(By.CSS_SELECTOR, '.person-BaseInfo')
    my_name.click()
    sleep(1)
    text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    text.send_keys('Ура!!! Мои первые автотесты!')
    text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    send = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__content-area [title="Отправить"]')
    send.click()
    sleep(1)
    message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item')
    assert message, 'Нет сообщения'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.perform()
    mes_del = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    mes_del.click()
    sleep(1)
    assert message != '', 'Сообщение не удалено'
    print('Тест №2 пройден!')
finally:
    driver.quit()
