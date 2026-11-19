"""Write a python program to accept a sentence, and using a dictionary display the frequency of each word. Also display the most frequent word."""

import string


def word_frequency(sentence):
    cleaned = sentence.lower().translate(str.maketrans("", "", string.punctuation))
    freq = {}
    for word in cleaned.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


sentence = input("Enter a sentence: ").strip()
if not sentence:
    print("No sentence entered ")
else:
    freq = word_frequency(sentence)
    if not freq:
        print("No words found ")
    else:
        print("\nWord frequencies:")
for word, count in sorted(freq.items(), key=lambda item: item[1], reverse=True):
    print(f"{word:<15} : {count}")

# most frequent word(s): handle ties by collecting every word with max count
max_count = max(freq.values())
top_words = [word for word, count in freq.items() if count == max_count]
print()
if len(top_words) == 1:
    print(f"Most frequent word: '{top_words[0]}' (appears {max_count} time.)")
else:
    print(f"Most frequent words (tie, {max_count} times each):{', '.join(top_words)}")
