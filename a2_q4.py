# 4. Write a Python program that accepts a hyphen-separated sequence of words as input 
# and  prints the words in a hyphen-separated sequence 
# after sorting them alphabetically.

def sort_hyphenated_sequence():
    # Accept hyphen-separated words from the user
    words = input("Enter a hyphen-separated sequence of words: ")

    # Split the input string into a list of words
    word_list = words.split('-')

    # Sort the list of words alphabetically
    word_list.sort()

    # Join the sorted list back into a hyphen-separated string
    sorted_words = '-'.join(word_list)

    # Print the sorted hyphen-separated sequence
    print("Sorted sequence:", sorted_words)

# Run the function
sort_hyphenated_sequence()





