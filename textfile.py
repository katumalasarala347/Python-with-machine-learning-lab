import string

def count_word_frequency(input_file, output_file):
    word_counts = {}

    try:
        # 1. Read the text file
        with open(input_file, 'r') as file:
            for line in file:
                # Preprocessing: lowercase and remove punctuation
                line = line.lower().translate(str.maketrans('', '', string.punctuation))
                words = line.split()

                # 2. Count frequencies using a dictionary
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1

        # 3. Save results to a new file
        with open(output_file, 'w') as file:
            file.write("Word: Frequency\n")
            file.write("-" * 20 + "\n")
            # Sort by frequency (highest first) for better insights
            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            
            for word, count in sorted_words:
                file.write(f"{word}: {count}\n")
        
        print(f"Success! Results saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")

# --- Execution ---
# Create a dummy file for testing if it doesn't exist
with open("data.txt", "w") as f:
    f.write("Machine learning is great. Learning python is also great!")

count_word_frequency("data.txt", "results.txt")