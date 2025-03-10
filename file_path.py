def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import math
    import os

    try:

        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/file_input.html"
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
        last_name.send_keys("Petrov")

        email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
        email.send_keys("asd@mail.ru")

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'file.txt')

        choose_file = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
        choose_file.send_keys(file_path)

        button = browser.find_element(By.CSS_SELECTOR, '.btn')
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    main()
