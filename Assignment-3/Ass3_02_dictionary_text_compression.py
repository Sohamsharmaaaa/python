"""Write a python script to input a filename and generate the another compressed file by replacing the
duplicate words with a single special character. Also add the dictionary at the end of the compressed
file as replaced_word: special symbol"""

filename = input("Enter file name ")
# Read the file and collect the words
with open(filename, "r") as file:
    lines = file.readlines()

# count how often each word appears
count = {}
for line in lines:
    for word in line.split():
        count[word] = count.get(word, 0) + 1

# Give each duplicat word a special symbol
symbols = {}
code = 0x2600  # start of the unicode " Miscellaneous Symbols" block
for word, c in count.items():
    if c > 1:
        symbols[word] = chr(code)
        code += 1

# write the compressed file
output_name = "compressed_" + filename
with open(output_name, "w", encoding="utf-8") as out:
    for line in lines:
        new_words = [symbols.get(word, word) for word in line.split()]
        out.write(" ".join(new_words) + "\n")

        # Add the dictionary at the end
    out.write("\n----- Dictionary ------------\n")
    for word, symbol in symbols.items():
        out.write(f"{word} : {symbol}\n")
print("Compressed file created: ", output_name)
