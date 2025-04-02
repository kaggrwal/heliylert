const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        headless: true, // Ensures no GUI issues
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();
    await page.goto('https://www.heliyatra.irctc.co.in/');

    // Example: Check if the "Book Ticket" button is enabled
    const isBookingOpen = await page.evaluate(() => {
        const button = document.querySelector('button');
        return button && !button.disabled;
    });

    console.log(isBookingOpen ? '🚨 Booking is OPEN! 🚨' : '❌ Booking is still CLOSED.');

    await browser.close();
})();
