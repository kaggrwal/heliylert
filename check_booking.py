from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

URL = "https://www.heliyatra.irctc.co.in/"

def check_booking_status():
    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Start Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Open the webpage
    driver.get(URL)

    # Wait for JavaScript content to load
    time.sleep(5)  # Increase if needed

    # Get page content
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find the button by text content
    buttons = soup.find_all("button")
    book_button = None
    for button in buttons:
        if "Book Ticket" in button.text:
            book_button = button
            break

    # Close browser
    driver.quit()

    if book_button:
        if "disabled" in book_button.attrs:
            print("❌ Bookings are still CLOSED.")
        else:
            print("🚨 Bookings are OPEN!")
    else:
        print("Could not find the 'Book Ticket' button.")

if __name__ == "__main__":
    check_booking_status()
