import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all patterns where we have data-lang="de" followed by data-lang="en"
pattern = r'<span data-lang="de">([^<]+)</span>\s*<span data-lang="en">([^<]+)</span>'
matches = re.findall(pattern, content)

# Print mismatches or specific issues
for de, en in matches:
    if len(de) > 2 and len(en) > 2:  # Skip very short ones
        print(f"DE: {de[:60]}")
        print(f"EN: {en[:60]}")
        print("---")
