"""Word Finder: finds random words from a dictionary."""

import random
import os
class WordFinder:
    def __init__(self):
        """Initialize WordFinder with the word database file 'words.txt' in the same folder as the script."""
        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.filepath = os.path.join(script_directory, "words.txt")
        self.words = self.load_words()
    
    def load_words(self):
        with open(self.filepath,'r') as file:
            return [word.strip() for word in file.readlines()]
        
    def random(self):
        random_word = random.choice(self.words)
        print(f"Random Dictionary word is: {random_word}")
        return random_word
    
    def search(self, keywords):
        return [word for word in self.words if keywords.lower() in word.lower()]
word_finder = WordFinder()
keyword = "apple"
matching_words = word_finder.search(keyword)
print(f"words containing '{keyword}':",matching_words)