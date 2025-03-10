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
        link = "http://suninjuly.github.io/redirect_accept.html"
        browser.get(link)

        button1 = browser.find_element(By.CSS_SELECTOR, '.trollface')
        button1.click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
        # print(x)
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
