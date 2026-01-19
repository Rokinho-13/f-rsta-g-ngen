const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function createPDFs() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  console.log('Skapar PDF-filer...\n');

  // 1. GEO Demo HTML -> PDF
  console.log('1/3 Konverterar geo-demo.html...');
  await page.goto('file://' + path.resolve('geo-demo.html'));
  await page.pdf({
    path: '/home/user/Desktop/GEO-Demo-Webbplats.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '20px', right: '20px', bottom: '20px', left: '20px' }
  });
  console.log('✓ GEO-Demo-Webbplats.pdf skapad');

  // 2. GEO-GUIDE.md -> PDF
  console.log('2/3 Konverterar GEO-GUIDE.md...');
  const geoGuide = fs.readFileSync('GEO-GUIDE.md', 'utf8');
  const geoGuideHtml = markdownToHtml(geoGuide, 'GEO Demo-webbplats - Guide');
  await page.setContent(geoGuideHtml);
  await page.pdf({
    path: '/home/user/Desktop/GEO-Guide.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '20px', right: '20px', bottom: '20px', left: '20px' }
  });
  console.log('✓ GEO-Guide.pdf skapad');

  // 3. GITHUB-PAGES-GUIDE.md -> PDF
  console.log('3/3 Konverterar GITHUB-PAGES-GUIDE.md...');
  const githubGuide = fs.readFileSync('GITHUB-PAGES-GUIDE.md', 'utf8');
  const githubGuideHtml = markdownToHtml(githubGuide, 'GitHub Pages - Aktiveringsguide');
  await page.setContent(githubGuideHtml);
  await page.pdf({
    path: '/home/user/Desktop/GitHub-Pages-Guide.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '20px', right: '20px', bottom: '20px', left: '20px' }
  });
  console.log('✓ GitHub-Pages-Guide.pdf skapad');

  await browser.close();

  console.log('\n✅ Alla PDF-filer är klara och ligger på ditt skrivbord!');
  console.log('📁 Plats: /home/user/Desktop/\n');
}

function markdownToHtml(markdown, title) {
  // Enkel markdown till HTML-konvertering
  let html = markdown
    // Headers
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
    // Bold
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    // Code blocks
    .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
    // Inline code
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    // Lists
    .replace(/^\- (.*$)/gim, '<li>$1</li>')
    .replace(/^(\d+)\. (.*$)/gim, '<li>$2</li>')
    // Links
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>')
    // Checkboxes
    .replace(/\[ \]/g, '☐')
    .replace(/\[x\]/gi, '☑')
    // Line breaks
    .replace(/\n\n/g, '</p><p>')
    // Horizontal rules
    .replace(/^---$/gim, '<hr>');

  return `
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>${title}</title>
      <style>
        body {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
          line-height: 1.6;
          color: #333;
          max-width: 800px;
          margin: 40px auto;
          padding: 20px;
        }
        h1 {
          color: #667eea;
          border-bottom: 3px solid #667eea;
          padding-bottom: 10px;
          margin-top: 30px;
        }
        h2 {
          color: #764ba2;
          margin-top: 25px;
          border-bottom: 2px solid #eee;
          padding-bottom: 8px;
        }
        h3 {
          color: #48bb78;
          margin-top: 20px;
        }
        code {
          background: #f4f4f4;
          padding: 2px 6px;
          border-radius: 3px;
          font-family: 'Courier New', monospace;
          font-size: 0.9em;
        }
        pre {
          background: #2d3748;
          color: #fff;
          padding: 15px;
          border-radius: 5px;
          overflow-x: auto;
        }
        pre code {
          background: none;
          color: #fff;
          padding: 0;
        }
        a {
          color: #667eea;
          text-decoration: none;
        }
        a:hover {
          text-decoration: underline;
        }
        li {
          margin: 8px 0;
        }
        ul, ol {
          margin: 10px 0;
          padding-left: 30px;
        }
        hr {
          border: none;
          border-top: 2px solid #eee;
          margin: 30px 0;
        }
        strong {
          color: #2d3748;
        }
      </style>
    </head>
    <body>
      <p>${html}</p>
    </body>
    </html>
  `;
}

createPDFs().catch(console.error);
