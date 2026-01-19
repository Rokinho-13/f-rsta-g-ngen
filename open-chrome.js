const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('http://localhost:8000/geo-demo.html');

  console.log('Chrome öppnad med geo-demo.html!');
  console.log('Tryck Ctrl+C för att stänga...');

  // Håll webbläsaren öppen
  await new Promise(() => {});
})();
