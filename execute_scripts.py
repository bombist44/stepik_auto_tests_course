def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import math

    try:

        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/execute_script.html"
        browser.get(link)

        x_value = browser.find_element(By.ID, "input_value")
        y = calc(int(x_value.text))

        form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
        form.send_keys(str(y))

        browser.execute_script("window.scrollBy(0, 100);")

        checkbox = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
        checkbox.click()

        radiobutton = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
        radiobutton.click()

        button = browser.find_element(By.CSS_SELECTOR, '.btn')
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
