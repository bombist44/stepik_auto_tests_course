def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import math

    try:

        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        link = "http://suninjuly.github.io/get_attribute.html"
        browser = webdriver.Chrome()
        browser.get(link)

        treasure = browser.find_element(By.ID, "treasure")

        value_x = treasure.get_attribute("valuex")

        y = calc(value_x)

        form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
        form.send_keys(str(y))

        checkbox = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
        checkbox.click()

        radiobutton = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
        radiobutton.click()

        button = browser.find_element(By.CSS_SELECTOR, '.btn')
        button.click()



    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
