import random
scores, replays = [], 6

def generate_rand() :
    global possible_nums
    x = random.choice(tuple(possible_nums))
    possible_nums = possible_nums.difference(set((x,)))
    return x

for y in range(1, replays+1) :
    possible_nums = {num for num in range(1,101)}
    win_num, death_num, guesses = generate_rand(), {generate_rand()}, 0
    print("There is a random number from 1 to 100. Try to guess it. There is another different random number from 1 to 100 which you can't guess. Every 3 failed guesses a new death number gets created. The game can be played 6 times. This is play number {}".format(y))
    while True :
        guess = input("Enter your guess: ")
        while not (guess.isdigit() and int(guess) > 0 and int(guess) <= 100):
            print("That's not a whole number between 1 and 100. Try again.")
            guess = input("Enter your guess: ")
        guess = int(guess)
        guesses += 1
        print("Guess number " + str(guesses))
        if guess == win_num :
            scores.append(guesses)
            print("Correct guess.\n\r\tYou win.")
            print("Score (lower is better) : " + str(guesses))
            print("High Score : " + str(min(scores)))
            break
        elif set((guess,)).issubset(death_num) :
            print("Uh oh, you hit the death number.\n\r\tYou lose")
            break
        offset = guess - win_num
        if offset > 10 :
            print("Too high, guess lower")
        elif offset < -10 :
            print("Too low, guess higher")
        elif offset > 0 :
            print("Slightly high, guess a little lower")
        elif offset < 0 :
            print("Slightly low, guess a little higher")
        if guesses % 3 == 0 :
            death_num.update(set((generate_rand(),)))
    if (y < replays) :
        input("Press enter to start the game again")