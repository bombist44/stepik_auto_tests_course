def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import math
    import os

    try:
        def calc(x):
            return math.log(abs(12 * math.sin(x)))

        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/alert_accept.html"
        browser.get(link)

        button1 = browser.find_element(By.CSS_SELECTOR, '.btn')
        button1.click()

        confirm = browser.switch_to.alert
        confirm.accept()

        x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
        print(x)
        y = calc(int(x.text))

        form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
        form.send_keys(str(y))

        button2 = browser.find_element(By.CSS_SELECTOR, '.btn')
        button2.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
