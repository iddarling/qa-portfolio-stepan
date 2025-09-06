from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_valid():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    driver.find_element(By.ID, "username").send_keys("test_user")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-button").click()

    assert "Dashboard" in driver.page_source
    driver.quit()
