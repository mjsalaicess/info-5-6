def main():
    welcome()
    get_item()


def welcome():
    menu = ["cheeseburger", "fries", "soda", "ice cream", "cookie"]
    print("Welcome to Big Back Town!!")
    print("Heres our very unhealthy menu to fill that hole in your heart with food: ")
    for i in range(len(menu)):
        print(f"{i+1} {menu[i]}")


def get_item():
    menu = ["cheeseburger", "fries", "soda", "ice cream", "cookie"]
    choice = input("What would you like to order?: ")
    if choice == "cheeseburger":
        print("Here you go! 🍔")
    elif choice == "fries":
        print("Here you go! 🍟")
    elif choice == "soda":
        print("Here you go! 🥤")
    elif choice == "ice cream":
        print("Here you go! 🍦")
    elif choice == "cookie":
        print("Here you go! 🍪")
    else:
        print("Please choose from the options available")



if __name__=="__main__":
    main()
