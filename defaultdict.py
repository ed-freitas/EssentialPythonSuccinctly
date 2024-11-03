from collections import defaultdict

# Initialize a defaultdict with default type of int (for counting)
word_count = defaultdict(int)

# Count occurrences of each word in a list
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    word_count[word] += 1

print("Word counts:", word_count)
