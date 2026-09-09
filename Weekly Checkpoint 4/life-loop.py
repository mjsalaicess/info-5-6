import time



def main():
    screen_t = int(input("How mant hours of screen time do you want to set? "))

    print(f"Perfect, you have {screen_t} hours of screen time today")







    while True:
        time.sleep(.900 * screen_t)
        print("You´re a quarter of the way through")

        time.sleep(.900 * screen_t)
        print("You´re half of the way through")


        time.sleep(.900 * screen_t)
        print("You´re three quarters of the way through")

        time.sleep(.900 * screen_t)


        while True:
            print("Times up")
            print("Times up")
            print("Times up")
            print("Times up")
            print("Times up")



if __name__ == "__main__":
    main()
