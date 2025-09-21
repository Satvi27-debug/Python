from collections import Counter

def find_most_frequent_word(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase for uniformity
            words = text.split()  # Split text into words

        word_counts = Counter(words)  # Count occurrences of each word
        most_common_word, most_common_count = word_counts.most_common(1)[0]

        print(f"Most frequent word: '{most_common_word}' (occurrences: {most_common_count})")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter file name: ")
find_most_frequent_word(filename)