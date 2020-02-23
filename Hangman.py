import pandas as pd
import random

df = pd.read_csv("movie_titles.csv")
df = df[['title']]

movies = df['title'].values.tolist()

for i in movies:
    if len(i) < 5:
        movies.remove(i) # Removing movies that have 4 letters or less

movie_list = [i.replace(' ', '').lower() for i in movies]

random_movie_index = random.randrange(len(movie_list))
random_movie = movie_list[random_movie_index]

correct_guesses = []

def answer(guess):
    if guess in random_movie:
        if guess not in guessed_elements:
            correct_guesses.append(guess)
            print('Correct Answer')
            return True
    if guess not in random_movie:
        if guess not in guessed_elements:
            print("Incorrect Answer")
            return False

#print(random_movie)       #For cross reference
print("Guess the movie: ")
letters = len(random_movie) * [' _ ']
print(''.join(letters))

guessed_elements = []

incorrect = 0
while incorrect < 5:
    guess = input('Enter the letter of the movie (or character/number) :')
    if len(guess) != 1:
        while len(guess) !=1:
            guess = input('Input only 1 letter at a time:')

    correct_or_not = answer(guess)

    guessed_elements.append(guess)
    print('Current Guesses: ', list(set(guessed_elements)))
    set_random_movie = set(random_movie)

    # x is the set containing the letters of the movie we are trying to guess,
    # while y is a list of all the correct guesses we have made.
    # So if x and y are equal that means our correct guesses include all the elements of the movie
    # we're trying to guess

    x = sorted(set_random_movie)
    y = sorted(correct_guesses)
    if x == y:
        print('You won! The movie was \"', movies[random_movie_index], '\"')
        break

    if correct_or_not == True:
        for count, movie_letter in enumerate(random_movie):
            if movie_letter == guess:
                letters[count] = guess

        print(''.join(letters))
    if correct_or_not == False:
        incorrect = incorrect + 1

if incorrect == 5:
    print("You lose!")
    print('The name of the movie was \"',movies[random_movie_index], '\"')