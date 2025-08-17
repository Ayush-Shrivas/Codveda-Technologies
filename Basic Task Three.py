# Word Counter Program

def word_counter(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Number of words: {len(words)}")
    except FileNotFoundError:
        print("Error: File not found.")

# Main program
filename = input("Enter the file name: ")
word_counter(filename)
