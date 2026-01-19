#!/usr/bin/env python3
"""
Skickar PDF-filer via email
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_pdfs():
    # Email-konfiguration
    to_email = "alexanderroka95@gmail.com"
    subject = "Dina GEO-konsult PDF-filer"

    # PDF-filer att skicka
    pdf_files = [
        "/home/user/Desktop/GEO-Demo-Webbplats.pdf",
        "/home/user/Desktop/GEO-Guide.pdf",
        "/home/user/Desktop/GitHub-Pages-Guide.pdf"
    ]

    # Skapa email
    msg = MIMEMultipart()
    msg['From'] = "Claude Assistant"
    msg['To'] = to_email
    msg['Subject'] = subject

    # Email-text
    body = """
Hej!

Här kommer dina 3 PDF-filer för ditt GEO-konsultföretag:

1. GEO-Demo-Webbplats.pdf (47 KB) - Din professionella demo-sida
2. GEO-Guide.pdf (85 KB) - Komplett guide med alla 3 GEO-tekniker
3. GitHub-Pages-Guide.pdf (62 KB) - Instruktioner för publicering online

Lycka till med din GEO-konsultresa! 🚀

/Claude
    """

    msg.attach(MIMEText(body, 'plain'))

    # Bifoga PDF-filer
    for filepath in pdf_files:
        if os.path.exists(filepath):
            filename = os.path.basename(filepath)
            print(f"Bifogar: {filename}")

            with open(filepath, "rb") as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={filename}')
            msg.attach(part)
        else:
            print(f"Varning: Hittade inte {filepath}")

    # Skicka email (kräver SMTP-server)
    try:
        # Standard Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        print("\n⚠️  För att skicka email behöver jag:")
        print("1. En fungerande SMTP-server")
        print("2. Email-konto med lösenord")
        print("\nJag kan tyvärr inte skicka email utan dessa uppgifter.")
        print("\nAlternativ:")
        print("- Kopiera PDF-filerna manuellt från /home/user/Desktop/")
        print("- Använd ditt eget email-program")
        print("- Ladda ner från GitHub")

        server.quit()

    except Exception as e:
        print(f"\n❌ Kunde inte skicka email: {e}")
        print("\nPDF-filerna finns på:")
        for pdf in pdf_files:
            print(f"  • {pdf}")

if __name__ == "__main__":
    send_pdfs()
