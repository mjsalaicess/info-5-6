        try:
            binary_number = float(input("Enter a binary number: "))
            if binary_number <=0:
                print("X")
            else:
                print("Invalid")
        except ValueError:
            print("You must enter a binary number: ")
