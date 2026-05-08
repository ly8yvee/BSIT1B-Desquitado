FILE_NAME = "dreams.txt"

while True:
    print("\n==== DREAMS FILE MANAGER ====\n")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        try:
            file = open(FILE_NAME, "r")
            content = file.read()

            print("\n--- Inspiring Messages ---")
            print(content)

            file.close()

        except FileNotFoundError:
            print("File does not exist.")

    elif choice == "2":
        new_message = input("Enter your new inspiring line: ")

        file = open(FILE_NAME, "a")
        file.write("\n" + new_message)
        file.close()

        print("\nYour inspiration has been added!")

    elif choice == "3":
        print("Warning: This will overwrite the file.")
        confirm = input("Type YES to continue: ")

        if confirm == "YES":
            print("Write your new set of inspiring messages:")
            new_content = input()

            file = open(FILE_NAME, "w")
            file.write(new_content)
            file.close()

            print("File has been overwritten.")
        else:
            print("Rewrite cancelled.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")

    print()