from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL = "https://www.heliyatra.irctc.co.in/"

def check_booking_status():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open the webpage
        driver.get(URL)

        # Wait until at least one button appears
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "button"))
        )

        # Get all buttons
        buttons = driver.find_elements(By.TAG_NAME, "button")

        # Debug: Print all button texts
        print("Found buttons:")
        for button in buttons:
            print("-", button.text.strip())

        # Find the 'Book Ticket' button
        book_button = None
        for button in buttons:
            if "Book Ticket" in button.text:
                book_button = button
                break

        if book_button:
            try:
                # Check if the button is clickable
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Book Ticket')]")))
                print("🚨 Bookings are OPEN! The 'Book Ticket' button is clickable.")
            except:
                print("❌ Bookings are still CLOSED. The 'Book Ticket' button is **disabled**.")
        else:
            print("❌ Could not find the 'Book Ticket' button.")

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    check_booking_status()
