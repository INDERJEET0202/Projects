# import random

# top_of_range = input("Type a number: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)

#     if top_of_range <= 0:
#         print('Please type a number larger than 0 next time.')
#         quit()
# else:
#     print('Please type a number next time.')
#     quit()

# random_number = random.randint(0, top_of_range)
# guesses = 0

# while True:
#     guesses += 1
#     user_guess = input("Make a guess: ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print('Please type a number next time.')
#         continue

#     if user_guess == random_number:
#         print("You got it!")
#         break
#     elif user_guess > random_number:
#         print("You were above the number!")
#     else:
#         print("You were below the number!")

# print("You got it in", guesses, "guesses")











import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


guess(10)