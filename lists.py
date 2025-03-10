def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    import time
    import math

    try:

        link = "http://suninjuly.github.io/selects1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        num1 = browser.find_element(By.ID, "num1")
        value_num1 = int(num1.text)
        num2 = browser.find_element(By.ID, "num2")
        value_num2 = int(num2.text)

        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value(str(value_num1 + value_num2))

        submit = browser.find_element(By.CSS_SELECTOR, '.btn')
        submit.click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
