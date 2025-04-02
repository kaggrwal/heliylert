const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        headless: true,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage'
        ]
    });

    const page = await browser.newPage();
    await page.goto('https://www.heliyatra.irctc.co.in/', { waitUntil: 'load' });

    // Check if the "Book Ticket" button is enabled
    const isBookingOpen = await page.evaluate(() => {
        const button = document.querySelector('button');
        return button && !button.disabled;
    });

    console.log(isBookingOpen ? '🚨 Booking is OPEN! 🚨' : '❌ Booking is still CLOSED.');

    await browser.close();
})();
