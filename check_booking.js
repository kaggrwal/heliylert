const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        headless: true, // Ensures no GUI issues
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
            '--disable-dev-shm-usage'
        ]
    });

    const page = await browser.newPage();
    await page.goto('https://www.heliyatra.irctc.co.in/');

    // Example: Check if the "Book Ticket" button is enabled
    const isBookingOpen = await page.evaluate(() => {
        const button = document.querySelector('button');
        return button && !button.disabled;
    });

    if (isBookingOpen) {
        console.log('🚨 Booking is OPEN! 🚨');
    } else {
        console.log('❌ Booking is still CLOSED.');
    }

    await browser.close();
})();
