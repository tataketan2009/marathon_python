import re
import os


os.makedirs("data", exist_ok=True)


with open("data/censored_words.txt", "w") as f:
    f.write("donkey\nidiot\nstupid\nfool")


with open("data/censored_words.txt", "w") as f:
    f.write("this is the sentence which should be changed into a censored version. "
            "The words 'Donkey', 'idiot', 'STUPID', and 'fool' will be replaced.")


with open("data/censored_words.txt", "r") as f:
    censored_words = [line.strip() for line in f if line.strip()]


with open("data/censored_words.txt", "r") as f:
    content = f.read()


for word in censored_words:
    # Use word boundaries (\b) and ignore case
    content = re.sub(r'\b' + re.escape(word) + r'\b', "#########", content, flags=re.IGNORECASE)

# 6. Write the censored text back to the same file
with open("data/censored_words.txt", "w") as f:
    f.write(content)

# 7. Verify
print("Censored text written to data/para.txt")
with open("data/censored_words.txt", "r") as f:
    print(f.read())