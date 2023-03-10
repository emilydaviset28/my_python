import random

words = ['python', 'java', 'ruby', 'javascript', 'php']
word = random.choice(words)
correct_letters = set()
incorrect_letters = set()
max_attempts = 6

while len(incorrect_letters) < max_attempts and len(correct_letters) < len(set(word)):
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters or guess in incorrect_letters:
        print("You already guessed that letter")
    elif guess in word:
        correct_letters.add(guess)
        print("Correct!")
    else:
        incorrect_letters.add(guess)
        print("Incorrect!")
    
    # Display the current state of the word
    word_state = ''
    for letter in word:
        if letter in correct_letters:
            word_state += letter
        else:
            word_state += '_'
    print(word_state)

if len(incorrect_letters) == max_attempts:
    print(f"Sorry, you lost. The word was {word}")
else:
    print("Congratulations, you won!")
