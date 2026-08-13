def main():
    # planet = input("Planet:")

    # # Seperation
    # print("Hello", planet)

    # #Concatenation
    # print("Hello "+ planet)

    # # Formatted Strings
    # print (f"Hello {planet}")

    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("What is your name? ").strip().title()
    color = input("Tell me a color: ").strip().lower()
    adj = input("Give me an adjective: ").strip().lower()
    goal = input ("What is a goal you want to achive? ").strip().lower()

    print (f"Hello, {name.strip()}!")
    print()

    print("This is your story:")
    print(f"At down the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.")


if __name__ == "__main__":
    main()

    name = input("What is your name? ").strip().title()
    color = input("Tell me a color: ").strip().lower()
    adj = input("Give me an adjective: ").strip().lower()
    goal = input ("What is a goal you want to achive? ").strip().lower()

    print (f"Hello, {name.strip()}!")
    print()

    print("This is your story:")
    print(f"At down the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.".strip().upper())


if __name__ == "__main__":
    main()
