#Find the Longest Word in a Sentence
#Finds the longest word from a given sentence.
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
print(find_longest_word("This is a test sentence"))
