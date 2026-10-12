def main():
    with open("sample.txt") as new_file:
        content = new_file.read()
        print(content)

    count = 0
    with open("sample_txt") as hoco_week:
        for line in hoco_week:
            line = line.replace(\n","")
            count += 1
            print(f"Day {count}; {line}")

if __name__=="__main__":
    main()
