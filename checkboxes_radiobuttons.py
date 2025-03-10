def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import math

    try:

        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        link = "https://suninjuly.github.io/math.html"
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
        x = x_element.text

        y = calc(x)
        # print(x, y)

        form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
        form.send_keys(str(y))

        checkbox = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
        checkbox.click()

        radiobuton = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
        radiobuton.click()

        button = browser.find_element(By.CSS_SELECTOR, '.btn')
        button.click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
