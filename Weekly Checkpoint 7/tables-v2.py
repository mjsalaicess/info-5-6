def main():
    print("Welcome to the Times Table Quiz!")

    while True:
        times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))

        if 1 <= times_table <= 10:
            max_value = int(input("Enter maximum value for the times table: "))

            print(f"Here is the {times_table} times table")

            for x in range(1, max_value +1):
                answer = x * times_table
                user_answer = int(input(f"{x} times {times_table} is: "))

                if user_answer == answer:
                    print("Correct!")

                elif user_answer != answer:
                    print("Incorrect :(")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
