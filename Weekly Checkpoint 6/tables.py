def main():
    while True:
        number = input("Enter a number(1-10):")
        if number != "exit":
            number = int(number)
            print(f"Here is the {number} times table")
            for i in range(1,11):
                result = i * number
                print (f"{i} times {number} is {result}")
        elif number == "exit":
            break

if __name__=="__main__":
    main()
