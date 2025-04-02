const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Open the booking website
    await page.goto('https://www.heliyatra.irctc.co.in/', { waitUntil: 'domcontentloaded' });

    // Wait for the button to load
    await page.waitForSelector("button", { timeout: 5000 });

    // Find the "Book Ticket" button
    const isBookingOpen = await page.evaluate(() => {
        const button = [...document.querySelectorAll("button")].find(btn => btn.textContent.includes("Book Ticket"));
        return button && !button.disabled; // Booking is open if the button is enabled
    });

    if (isBookingOpen) {
        console.log("🚨 Booking is OPEN! 🚨");
    } else {
        console.log("❌ Booking is still CLOSED.");
    }

    await browser.close();
})();
