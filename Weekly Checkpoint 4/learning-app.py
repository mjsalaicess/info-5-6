import random
def main():
    print ("Welcome to Brilliant from the hood!")
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    addition = num1 + num2

    print(f"What is {num1} + {num2}?")
    answer = int(input("Your answer: "))

    if answer==addition:
        print("Well done!")
    elif answer != addition:
        print("Almost there! Try Again")
        print(f"The answer was {addition}")


if __name__=="__main__":
    main()
