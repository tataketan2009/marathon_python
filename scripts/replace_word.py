with open('data/para.txt', 'w') as file:
    file.write("This is a sample paragraph. This paragraph is used for testing the replace word functionality. The word 'paragraph'  donkey will be replaced with 'sentence' in this text.")

with open('data/para.txt', 'r') as file:
    if "donkey" in file.read().casefold():
        replace_word = "donkey"
        replace_text = "#########"
        with open('para.txt', 'r') as file:
            content = file.read()
        if replace_word in content.casefold():
            content = content.replace(replace_word, replace_text)
            with open('data/para.txt', 'w') as file:
                file.write(content)
        print("The word 'donkey' is present in the file.")


with open('data/para.txt', 'r') as file:
    s = file.read()
    print(s)