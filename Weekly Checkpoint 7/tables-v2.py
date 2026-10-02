def main():
    valid_num = []
    for i in range (1,11):
        valid_num.append (str(i))
    while True:
        print("Welcome to a times table quiz")
        times_table = input("Enter a times table that you would like to be tested on: ")
        break
        

    if times_table in valid_num:
        max_value = int(input("Enter maximun value for the times table: "))
        print("Here is your quiz in the {times_table} times table")
        for x in range(1,max_value +1):
            answer = x * int(times_table)
            print(f"{times_table} x {x}")
            user_answer = int(input("Type an answer: "))
            if user_answer == answer:
                print("Correct!")
            else:
                print("Incorrect")

if __name__=="__main__":
    main()
