import random
def main():
    flip = random.randint(1, 2)

    if flip == 1:
        print("Heads")
    elif flip == 2:
        print("Tales")

if __name__=="__main__":
    main()
