import re

text = "<p>Hello World! This is some text.</p>"

# Your regex cleaning steps
text = re.sub(r"<.*?>", "", text)
text = re.sub(r"[^a-zA-Z\s]", "", text)
text = re.sub(r"\s+", " ", text).strip()

print(text)