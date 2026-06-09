#Write a program that takes a sentence from the user and counts the number of unique words.
sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set(words)

print("Number of unique words:", len(unique_words))

print("Unique words:")
for word in unique_words:
    print(word)