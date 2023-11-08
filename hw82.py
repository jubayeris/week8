file_name = "romeo.txt"

try:
    with open(file_name, 'r') as file:
        unique_words = set()
        for line in file:
            words = line.split()
            for word in words:
                unique_words.add(word.lower())

        sorted_unique_words = sorted(unique_words)
        for word in sorted_unique_words:
            print(word)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")