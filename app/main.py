import fitz  # PyMuPDF
import os
import json
import re

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []

    title = os.path.splitext(os.path.basename(pdf_path))[0]

    heading_pattern = re.compile(r"^(#{1,6})\s+(.*)")

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        lines = text.split('\n')
        for line in lines:
            match = heading_pattern.match(line.strip())
            if match:
                hashes, content = match.groups()
                level = f"H{len(hashes)}"
                outline.append({
                    "level": level,
                    "text": line.strip(),
                    "page": page_num
                })

    return {"title": title, "outline": outline}

def main():
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            result = extract_outline(pdf_path)

            json_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(output_dir, json_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()