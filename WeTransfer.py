from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time

def transfer(driver_path, email, password, send_to_list, email_message, processed_path, processed_files):
    start_time = time.time()
    service = Service(executable_path=driver_path)
    driver = webdriver.Firefox(service=service)
    driver.get('https://wetransfer.com/log-in')
    time.sleep(10)
    email_field = driver.find_element(By.XPATH, '//*[@id="1-email"]')
    email_field.clear()  # Clear any pre-filled value
    email_field.send_keys(email)  # Replace with the actual email
    submit_button = driver.find_element(By.XPATH, '//*[@id="1-submit"]')  # XPath for submit button
    submit_button.click()
    time.sleep(5)
    password_field = driver.find_element(By.XPATH, '//*[@id="1-password"]')
    password_field.clear()  # Clear any pre-filled value
    password_field.send_keys(password)  # Replace with the actual email
    submit_button = driver.find_element(By.XPATH, '//*[@id="1-submit"]')  # XPath for submit button
    submit_button.click()
    time.sleep(10)
    terms_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/button')  # XPath for submit button
    terms_button.click()
    time.sleep(5)
    for x in send_to_list:
        email_to = driver.find_element(By.XPATH, '//*[@id="autosuggest"]')  # XPath for submit button
        email_to.clear()  # Clear any pre-filled value
        email_to.send_keys(x)  # Replace with the actual email
    message_field = driver.find_element(By.XPATH, '//*[@id="message"]')
    message_field.clear()
    message_field.send_keys(email_message)
    for x in processed_files:
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"][webkitdirectory]')
        folder_path = fr'{processed_path}\{x}'
        file_input.send_keys(folder_path)
        time.sleep(5)
    send_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div/div[2]/button[2]')
    send_button.click()
    time.sleep(10)
    driver.quit()
    print(f'Processing Time: {((time.time() - start_time).__round__(2))} Seconds')