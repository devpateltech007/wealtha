import re

# Function to clean and normalize strings (remove symbols, ignore case)
def normalize(text):
    return re.sub(r'\W+', ' ', text.lower()).split()  # Split into words after removing symbols

# Function to check if all search words are in the line (in any order)
def contains_jumbled_words(search_words, line_words):
    return all(word in line_words for word in search_words)

# Function to find a string in the document
def find_in_textFile(search_term: str) -> list:

    found_links = []
    # Normalize and split the search term into words
    normalized_search_words = normalize(search_term)

    # Step 2: Reopen the file in read mode to search for the term (ignoring case and symbols)
    with open('news-urls.txt', 'r') as file:
        for line in file:
            # Normalize and split each line into words
            normalized_line_words = normalize(line)
            
            # Check if the line contains all words in the search term, regardless of order
            if contains_jumbled_words(normalized_search_words, normalized_line_words):
                # print(f"Found in line: {line.strip()}")
                found_links.append(line.strip())
    return found_links
                

