def merge_files(file1, file2, output_file):
    try:
        # Open both input files and the output file
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            out.write(f1.read() + "\n")  # Read and write content of first file
            out.write(f2.read())  # Read and write content of second file
        print(f"Files {file1} and {file2} merged successfully into {output_file}.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
output_file = input("Enter output file name: ")

merge_files(file1, file2, output_file)