def add_commas(word):
    return ",".join(word)

def remove_word(sentence, word):
    words = sentence.split()
    filtered_words = [w for w in words if w != word]
    return " ".join(filtered_words)

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = []
    
    for word in words:
        if len(word) > 0:
            capitalized_word = word[0].upper() + word[1:].lower()
            capitalized_words.append(capitalized_word)
    
    return " ".join(capitalized_words)

# User Inputs
word = input("Enter a word: ")
sentence = input("Enter a sentence: ")
remove_this = input("Enter the word to remove: ")

# Results
print("Comma-separated word:", add_commas(word))
print("Sentence after removing word:", remove_word(sentence, remove_this))
print("Capitalized sentence:", capitalize_words(sentence))