"""
Program: setenceGenerator.py
Chapter 5 Case Study ( pages 129- 132)
9/14/26

Application that generates and displays sentences using simple grammar. Each small process will be its own function. The user will input the number of sentences to generate. Words are chosen at random.
"""

import random

# Global variables containing the tuple lists with different parts of speech that ALL our functions can use
articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL", "DOG", "CAT","TURTLE", "LAPTOP", "PIZZA", "CAR", "TABLE")

verbs = ("HIT", "SAW", "LIKE", "JUMP", "ATE", "RAN", "FELL", "SNEEZED")

prepositions = ("WITH", "BY", "AT", "BETWEEN", "AROUND","IN", "ABOVE", "BELOW")

# Definition of a sentence() function
def sentence():
    '''Builds and returns a sentence.'''
    return nounPhrase() + " " + verbPhrase()

# Definition of a nounPhrase() function
def nounPhrase():
    '''Builds and returns a noun phrase.'''
    return random.choice(articles) + " " + random.choice(nouns)

# Definition of a verbPhrase() function
def verbPhrase():
    '''Builds and returns a verb phrase.'''
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

# Definition of a prepositionalPhrase() function
def prepositionalPhrase():
    '''Builds and returns a prepositional phrase.'''
    return random.choice(prepositions) + " " + nounPhrase()

# Definition of a main() function for program entry
def main():
    '''Prompts the user for the number of sentences to generate'''
    number = int(input("Please enter the number of sentences you'd like to see >> "))
    for count in range(number):
        print(sentence())
    # Loop is done, but we're still in main()
    input("\nSentences completed. Press ENTER to quit")

# Global call to the main() function for program execution
if __name__ == "__main__":
    main()
	

