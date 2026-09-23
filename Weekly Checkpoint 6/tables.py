def main():
    number = int(input("Enter a number(1-10):"))
    print(f"Here is the {number} times table")
    for i in range(1,11):
        result = i * number
        print (f"{i} times {number} is {result}")


if __name__=="__main__":
    main()
