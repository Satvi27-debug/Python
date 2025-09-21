def search_words_in_file(filename, words):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file

        # Find words in the content
        found_words = [word for word in words if word in content]

        if found_words:
            print("Found words:", ", ".join(found_words))
        else:
            print("No given words found in the file.")
            
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter file name: ")
words = input("Enter words to search (comma-separated): ").split(',')
words = [word.strip() for word in words]  # Remove extra spaces from the words list
search_words_in_file(filename, words)