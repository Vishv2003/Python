# Count Frequency of Words in a String
# Counts the occurrences of each word in a given string and returns a dictionary with word frequencies.
def count_word_frequencies(input_string):
    words = input_string.split()
    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies
input_string = "hello world hello"
print(count_word_frequencies(input_string))
