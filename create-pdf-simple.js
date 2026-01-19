const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

async function createPDFs() {
  // Försök hitta Chrome
  const possiblePaths = [
    '/usr/bin/google-chrome',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    '/opt/google/chrome/chrome',
    process.env.CHROME_BIN,
  ].filter(Boolean);

  let browser;
  for (const chromePath of possiblePaths) {
    try {
      if (fs.existsSync(chromePath)) {
        console.log(`Försöker med: ${chromePath}`);
        browser = await puppeteer.launch({
          executablePath: chromePath,
          headless: true,
          args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        break;
      }
    } catch (e) {
      continue;
    }
  }

  if (!browser) {
    console.error('❌ Kunde inte hitta Chrome/Chromium');
    console.log('\n📝 LÖSNING: Öppna HTML-filerna i din webbläsare och tryck Ctrl+P för att spara som PDF');
    console.log('\nFiler på ditt skrivbord:');
    console.log('1. GEO-Demo-Webbplats.html');
    console.log('2. GEO-Guide-Print.html');
    console.log('3. GitHub-Pages-Guide-Print.html');
    return;
  }

  const page = await browser.newPage();

  // 1. GEO Demo
  console.log('Skapar GEO-Demo-Webbplats.pdf...');
  await page.goto('file://' + path.resolve('/home/user/Desktop/GEO-Demo-Webbplats.html'));
  await page.pdf({
    path: '/home/user/Desktop/GEO-Demo-Webbplats.pdf',
    format: 'A4',
    printBackground: true,
  });

  // 2. GEO Guide
  console.log('Skapar GEO-Guide.pdf...');
  await page.goto('file://' + path.resolve('/home/user/Desktop/GEO-Guide-Print.html'));
  await page.pdf({
    path: '/home/user/Desktop/GEO-Guide.pdf',
    format: 'A4',
    printBackground: true,
  });

  // 3. GitHub Pages Guide
  console.log('Skapar GitHub-Pages-Guide.pdf...');
  await page.goto('file://' + path.resolve('/home/user/Desktop/GitHub-Pages-Guide-Print.html'));
  await page.pdf({
    path: '/home/user/Desktop/GitHub-Pages-Guide.pdf',
    format: 'A4',
    printBackground: true,
  });

  await browser.close();
  console.log('\n✅ PDF-filer skapade på /home/user/Desktop/');
}

createPDFs().catch(console.error);
