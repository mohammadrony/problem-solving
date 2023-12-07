import os
import re
import csv
import string


# Read Content
def read_list_from_csv(filename):
    stories = []
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)
        print(fields)
        i = 0
        for row in csvreader:
            stories.append(row[2])
            stories.append(row[5])
            # if(i < 1): i += 1
            # else: break

        return stories


# String Tokenization
def token_strings(stories):
    for i, story in enumerate(stories):
        story = story.translate(str.maketrans("", "", string.punctuation))
        story = story.translate(str.maketrans("", "", string.ascii_letters))
        story = story.replace("।", "")
        story = re.sub("\s+", " ", story)
        story = story.split()
        stories[i] = story

    stories_words = []
    for i, story in enumerate(stories):
        new_list = []
        for word in story:
            if re.findall("^[\u0985-\u09E5]+$", word):
                new_list.append(word)
        stories_words.append(new_list)
    return stories_words


# Write in CSV
def write_list_in_csv(lists, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as new_file:
        file_writer = csv.writer(
            new_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        for item in lists:
            str1 = ""
            if type(item[0]) is str:
                str1 = item[0]
            else:
                for word in item[0]:
                    str1 += word + " "
            file_writer.writerow([str1.strip(), item[1]])


# Unigram
def unigram(stories):
    os.system("mkdir -p Unigram")
    unigram_set = {}
    for story in stories:
        for word in story:
            unigram_set[word] = unigram_set.get(word, 0) + 1

    sorted_unigram_alpha = sorted(unigram_set.items(), key=lambda it: it[0])
    sorted_unigram_freq = sorted(
        unigram_set.items(), key=lambda it: it[1], reverse=True
    )

    write_list_in_csv(sorted_unigram_alpha, "Unigram/2-unigram-words-alphabet.csv")
    write_list_in_csv(sorted_unigram_freq, "Unigram/1-unigram-words-frequency.csv")


# Bigram
def bigram(stories):
    os.system("mkdir -p Bigram")
    bigram_set = {}
    for story in stories:
        if len(story) < 2:
            continue

        for i, word in enumerate(story):
            if i + 1 < len(story):
                two_words = (word, story[i + 1])
                bigram_set[two_words] = bigram_set.get(two_words, 0) + 1

    sorted_bigram_alpha = sorted(bigram_set.items(), key=lambda it: it[0])
    sorted_bigram_freq = sorted(bigram_set.items(), key=lambda it: it[1], reverse=True)

    write_list_in_csv(sorted_bigram_alpha, "Bigram/2-bigram-words-alphabet.csv")
    write_list_in_csv(sorted_bigram_freq, "Bigram/1-bigram-words-frequency.csv")


# Trigram
def trigram(stories):
    os.system("mkdir -p Trigram")
    trigram_set = {}
    for story in stories:
        if len(story) < 3:
            continue

        for i, word in enumerate(story):
            if i + 3 < len(story):
                three_words = (word, story[i + 1], story[i + 2])
                trigram_set[three_words] = trigram_set.get(three_words, 0) + 1

    sorted_trigram_alpha = sorted(trigram_set.items(), key=lambda it: it[0])
    sorted_trigram_freq = sorted(
        trigram_set.items(), key=lambda it: it[1], reverse=True
    )

    write_list_in_csv(sorted_trigram_alpha, "Trigram/2-trigram-words-alphabet.csv")
    write_list_in_csv(sorted_trigram_freq, "Trigram/1-trigram-words-frequency.csv")


stories = read_list_from_csv("story-contents.csv")
stories_words = token_strings(stories)
unigram(stories_words)
print("unigram processing done")
bigram(stories_words)
print("bigram processing done")
trigram(stories_words)
print("trigram processing done")
