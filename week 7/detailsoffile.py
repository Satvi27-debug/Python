def analyze_text(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()  # Read the content of the file
            
            # Calculate the number of words
            num_words = len(text.split())
            
            # Count the number of vowels (case-insensitive)
            num_vowels = sum(1 for char in text.lower() if char in 'aeiou')
            
            # Count the number of spaces
            num_spaces = text.count(' ')
            
            # Count the number of lowercase letters
            num_lowercase = sum(1 for char in text if char.islower())
            
            # Count the number of uppercase letters
            num_uppercase = sum(1 for char in text if char.isupper())
            
            # Print the results
            print(f"Number of words: {num_words}")
            print(f"Number of vowels: {num_vowels}")
            print(f"Number of blank spaces: {num_spaces}")
            print(f"Number of lowercase letters: {num_lowercase}")
            print(f"Number of uppercase letters: {num_uppercase}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter file name: ")
analyze_text(filename)