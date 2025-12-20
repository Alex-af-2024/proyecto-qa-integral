from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_saucedemo():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.saucedemo.com")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert "inventory.html" in driver.current_url
        print("✓ Se confirma acceso a url inventario de tienda.")
        print(f"✓ URL actual {driver.current_url}")

    except AssertionError:
        print("x ERROR: La URL no contiene 'inventory.html'")
        print(f"x URL actual {driver.current_url}")
        raise
    except Exception as e:
        print(f"✗ ERROR inesperado: {e}")
        raise

    finally:
        time.sleep(7)
        driver.quit()


test_login_saucedemo()