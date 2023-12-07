with open("text/words.txt", mode="r") as file1:
    all_words = []
    for line in file1.readlines():
        words = line.strip().split(" ")
        all_words += words

    uniq_words = set(all_words)
    print(len(all_words))
    print(len(uniq_words))

with open("text/uniq_words.txt", mode="w") as file2:
    for word in sorted(uniq_words):
        file2.write(word + " ")
