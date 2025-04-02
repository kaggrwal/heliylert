import requests
from bs4 import BeautifulSoup

URL = "https://www.heliyatra.irctc.co.in/"

def check_booking_status():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the button by text content (to ensure we get the correct button)
    buttons = soup.find_all("button")
    book_button = None
    for button in buttons:
        if "Book Ticket" in button.text:
            book_button = button
            break

    if book_button:
        if "disabled" in book_button.attrs:
            print("❌ Bookings are still CLOSED.")
        else:
            print("🚨 Bookings are OPEN!")
    else:
        print("Could not find the 'Book Ticket' button.")

if __name__ == "__main__":
    check_booking_status()
