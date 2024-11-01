# test_services.py

import os
import sys
from services import get_word_meaning, get_example_usage

def main():
    # Check if OPEN_AI_KEY is set
    if not os.getenv("OPEN_AI_KEY"):
        print("Error: The environment variable OPEN_AI_KEY is not set.")
        sys.exit(1)
    
    while True:
        word = input("Enter a word to get its meaning and an example usage (or type 'exit' to quit): ").strip()
        
        if word.lower() == 'exit':
            print("Exiting the test script.")
            break
        
        if not word:
            print("Please enter a valid word.")
            continue

        print("\nFetching data...\n")

        meaning = get_word_meaning(word)
        example = get_example_usage(word)

        if meaning:
            print(f"Meaning of '{word}': {meaning}")
        else:
            print(f"Could not fetch the meaning for '{word}'.")

        if example:
            print(f"Example usage: {example}")
        else:
            print(f"Could not fetch an example usage for '{word}'.")

        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
