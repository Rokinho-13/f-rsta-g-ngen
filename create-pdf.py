#!/usr/bin/env python3
"""
Skapar PDF-filer från HTML-dokument med weasyprint
"""

from weasyprint import HTML
import os

def create_pdfs():
    print("🎨 Skapar PDF-filer med weasyprint...\n")

    desktop = "/home/user/Desktop"
    project = "/home/user/f-rsta-g-ngen"

    pdfs = [
        {
            "input": f"{project}/geo-demo.html",
            "output": f"{desktop}/GEO-Demo-Webbplats.pdf",
            "name": "GEO Demo-webbplats"
        },
        {
            "input": f"{desktop}/GEO-Guide-Print.html",
            "output": f"{desktop}/GEO-Guide.pdf",
            "name": "GEO Guide"
        },
        {
            "input": f"{desktop}/GitHub-Pages-Guide-Print.html",
            "output": f"{desktop}/GitHub-Pages-Guide.pdf",
            "name": "GitHub Pages Guide"
        }
    ]

    for i, pdf_info in enumerate(pdfs, 1):
        try:
            print(f"[{i}/{len(pdfs)}] Skapar {pdf_info['name']}...")

            # Kolla att input-filen finns
            if not os.path.exists(pdf_info['input']):
                print(f"    ⚠️  Filen hittades inte: {pdf_info['input']}")
                continue

            # Skapa PDF
            HTML(filename=pdf_info['input']).write_pdf(pdf_info['output'])

            # Kolla filstorlek
            size = os.path.getsize(pdf_info['output'])
            size_kb = size / 1024

            print(f"    ✅ Klar! ({size_kb:.1f} KB)")

        except Exception as e:
            print(f"    ❌ Fel: {e}")

    print("\n" + "="*60)
    print("✅ PDF-FILER SKAPADE!")
    print("="*60)
    print(f"\n📁 Plats: {desktop}/\n")
    print("Filer:")
    print("  • GEO-Demo-Webbplats.pdf")
    print("  • GEO-Guide.pdf")
    print("  • GitHub-Pages-Guide.pdf")
    print("\n🎉 Nu kan du öppna, dela och skriva ut dina PDF-filer!")
    print("="*60 + "\n")

if __name__ == "__main__":
    create_pdfs()
