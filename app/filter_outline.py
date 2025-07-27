# app/filter_outline.py

import json

def load_outline(path="output/outline.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_outline(data, persona, job_to_be_done):
    keywords = (persona + " " + job_to_be_done).lower().split()
    filtered = []

    for item in data.get("outline", []):
        text = item["text"].lower()
        if any(keyword in text for keyword in keywords):
            filtered.append(item)

    return {
        "title": data.get("title", ""),
        "persona": persona,
        "job_to_be_done": job_to_be_done,
        "filtered_outline": filtered
    }

def main():
    persona = "Data Scientist"
    job_to_be_done = "Find relevant methodology and datasets"

    data = load_outline()
    result = filter_outline(data, persona, job_to_be_done)

    with open("output/filtered_outline.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("✅ Filtered outline saved to: output/filtered_outline.json")

if __name__ == "__main__":
    main()
