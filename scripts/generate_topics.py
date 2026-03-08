import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CATEGORY_DIR = BASE_DIR / "categories"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "topics.txt"

topics = []

for file in CATEGORY_DIR.glob("*.txt"):
    lines = file.read_text(encoding="utf-8").splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    if lines:
        topic = random.choice(lines)
        topics.append(f"[{file.stem}] {topic}")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text("\n".join(topics), encoding="utf-8")

print("Topics generated in output/topics.txt")
