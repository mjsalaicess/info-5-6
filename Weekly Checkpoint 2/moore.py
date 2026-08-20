def main ():
    transitors = 17.8
    years = int(input("How many years into the future? "))
    transitors *= round(2** (years/2))
    print(f"{transitors:,} billion")

if __name__=="__main__":
    main()
