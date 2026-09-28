def main():
    not_validated = True

    while not_validated:
        try:
            int(input("Enter a number between 1 and 10: "))
            not_validated = False
        except ValueError:
             print("You must enter a number between 1 and 10.")
        if not_validated == range(1,11):
            print("Number out of range")


if __name__=="__main__":
    main()
