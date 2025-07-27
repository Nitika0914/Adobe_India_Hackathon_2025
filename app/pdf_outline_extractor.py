# app/pdf_outline_extractor.py

import os
import sys
import json
from PyPDF2 import PdfReader

def extract_outline_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    outline = []

    title = os.path.basename(pdf_path).replace(".pdf", "")

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue

        lines = text.splitlines()

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue

            # Heuristic-based detection of headings
            if stripped.isupper():
                level = "H1"
            elif len(stripped.split()) <= 6:
                level = "H2"
            else:
                level = "H3"

            outline.append({
                "page": i + 1,
                "text": stripped,
                "level": level
            })

    return {
        "title": title,
        "outline": outline
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf_outline_extractor.py <input-pdf-path>")
        sys.exit(1)

    input_pdf = sys.argv[1]

    if not os.path.exists(input_pdf):
        print(f"❌ File not found: {input_pdf}")
        sys.exit(1)

    result = extract_outline_from_pdf(input_pdf)

    os.makedirs("output", exist_ok=True)
    with open("output/outline.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("✅ Outline saved to: output/outline.json")

if __name__ == "__main__":
    main()
