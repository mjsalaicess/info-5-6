import random
def main():
    start_game("random_words.txt")

def start_game(file):
    with open(file) as random_word:
        content = random_word.read().splitlines()
        secret_v = random.choice(content)
    print(secret_w)

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

