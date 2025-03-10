def main():
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver
    import time
    import math
    import os

    try:
        def calc(x):
            return math.log(abs(12 * math.sin(x)))

        browser = webdriver.Chrome()
        # говорим WebDriver искать каждый элемент в течение 5 секунд
        browser.implicitly_wait(5)
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser.get(link)

        price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

        button = browser.find_element(By.ID, "book")
        button.click()

        x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
        # print(x)
        y = calc(int(x.text))

        form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
        form.send_keys(str(y))

        button2 = browser.find_element(By.ID, 'solve')
        button2.click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
