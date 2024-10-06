import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
# keep the browser open gererating a new instance
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options)
# wait at least 10 seconds every time it navigate to another page
browser.implicitly_wait(20)
browser.get("https://hiraoka.com.pe/")
link = browser.find_element(By.CLASS_NAME, "hiraoka-login")
link.click()
link = browser.find_element(By.LINK_TEXT, "Inicia sesión")
link.click()
user_input = browser.find_element(By.ID, "email")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys(os.environ.get("HIRAOKA_EMAIL"))
pass_input.send_keys(os.environ.get("HIRAOKA_PASSWORD"))
pass_input.send_keys(Keys.RETURN)


def text_is_not_empty(driver):
    span_element = driver.find_element(
        By.CSS_SELECTOR, ".customer-name > span")
    return span_element.text != ""


# Wait for text
WebDriverWait(browser, 10).until(text_is_not_empty)

profile = browser.find_element(By.CSS_SELECTOR, ".customer-name > span")
profile_name = profile.text
print(profile_name)

assert "Rolando Priale" == profile_name, "the profile name is incorrect"

# close the browser
browser.quit()
