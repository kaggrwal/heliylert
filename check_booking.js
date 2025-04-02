const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({
        headless: true,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ]
    });
    const page = await browser.newPage();
    await page.goto('https://www.heliyatra.irctc.co.in/', { waitUntil: 'load' });

    // Check for the "Book Ticket" button status
    const isBookingOpen = await page.$eval('button', button => !button.disabled);
    console.log(isBookingOpen ? '🚨 Booking is OPEN! 🚨' : '❌ Booking is still CLOSED.');

    await browser.close();
})();
