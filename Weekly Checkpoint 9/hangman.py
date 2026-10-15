import random
def main():
    start_game("random_words.txt")

def start_game(file):
    attempts = 10
    with open(file) as random_word:
        content = random_word.read().splitlines()
        secret_w = random.choice(content)
        hint = (["_"] * len(secret_w))
        incorrect_letters = []
    while attempts > 0:
        print("Welcome to hangman game!")
        print("This is your word: ")
        print(" ".join(hint))

        while True:
            guess = input("Take a guess: ")
            if len(guess) == 1:
                break
            else:
                print("Invalid guess, type just ONE letter")

        if guess in secret_w and guess not in hint:
            for i in range(len(secret_w)):
                if secret_w[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")

        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", secret_w)
            break

        if attempts == 0 and "_" in hint:
            print("No attempts left 💀 The word was:", secret_w)



if __name__=="__main__":
    main()







#Define main function
#Create txt file that contains random words
#Define a start_game function with 1 parameter
#Open the txt file in our start_game function
#Convert our txt file into a list
#Ask the program to choose one of the random words
#Add a limit of tries
#Create an if if they get it right or wrong
#Do the same wit elif
#Do the same with else

#Start asking the user for their guesses


