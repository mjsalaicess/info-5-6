def main():
    atmosphere = input("Descent atmosphere layer:").strip().title()
    if atmosphere == "Exosphere":
        print("Your altitude level will be betweeen 700 and 10,000 km")
    elif atmosphere == "Thermosphere":
        print("Your altitude level will be betweeen 85 and 700 km")
    elif atmosphere == "Mesosphere":
        print("Your altitude level will be betweeen 50 and 85 km")
    elif atmosphere == "Stratosphere":
        print("Your altitude level will be betweeen 12 and 50 km")
    elif atmosphere == "Troposphere":
        print("Your altitude level will be betweeen 0 and 10 km")
    else:
        print("Invalid. Try again.")

    start = float(input("Enter exact altitude:"))





if __name__=="__main__":
    main()
