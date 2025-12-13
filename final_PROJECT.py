import os
import time

def menu():
    print("\n" + "="*30)
    print("\tPYTHON MENU DO")
    print("="*30)
    print("1. What is Python?")
    print("2. How to Install Python?")
    print("3. Python Basics")
    print("4. Data Types")
    print("5. Loops and Functions")
    print("6. Simple Quiz")
    print("7. Python Tips")
    print("8. Fun Facts")
    print("9. Exit")
    print("Pick a number (1-9): ")
    print("="*30)

def uno():
    print("\n" + "="*35)
    print("QUESTION: What is Python?")
    print("="*35)
    print("ANSWER:")
    print("Python is a easy programming language.")
    print("It is used for making websites, games, and more.")
    print("Created in 1991 by Guido van Rossum.")
    print("Python is free and open-source.")
    print("It runs on many computers like Windows, Mac, and Linux.")
    print("Many big companies use Python, like Google and Netflix.")
    print("="*35)

def dosht():
    print("\n" + "-"*32)
    print("QUESTION: How to Install Python?")
    print("-"*32)
    print("ANSWER:")
    print("1. Go to python.org/downloads")
    print("2. Download for your computer (Windows/Mac/Linux)")
    print("3. Run the installer.")
    print("4. Check 'Add to PATH' if asked.")
    print("5. Open command prompt and type: python --version")
    print("If it shows a version, it's installed!")
    print("You can also use IDLE, which comes with Python.")
    print("-"*32)

def tresht():
    print("\n" + "*"*30)
    print("QUESTION: What are Python Basics?")
    print("*"*30)
    print("ANSWER:")
    print("- Variables: Like boxes to store things. Example: x = 5")
    print("- Print: To show messages. Example: print('Hi')")
    print("- Comments: Notes in code. Start with #")
    print("- Indentation: Use 4 spaces for blocks.")
    print("Example code:")
    print("  # This is a comment")
    print("  name = 'Student'")
    print("  print('Hello, ' + name)")
    print("*"*30)

def quatro():
    print("\n" + "="*28)
    print("QUESTION: What are Data Types?")
    print("="*28)
    print("ANSWER:")
    print("- int: Whole numbers. Example: age = 10")
    print("- str: Words. Example: name = 'John'")
    print("- list: List of things. Example: fruits = ['apple', 'banana']")
    print("- bool: True or False. Example: is_big = True")
    print("You can change types, like int to str.")
    print("Example: str(10) becomes '10'")
    print("="*28)

def cinco():
    print("\n" + "-"*34)
    print("QUESTION: What are Loops and Functions?")
    print("-"*34)
    print("ANSWER:")
    print("- Loops: Repeat things. For loop: for i in range(3): print(i)")
    print("- Functions: Reusable code. def say_hi(): print('Hi')")
    print("Call it: say_hi()")
    print("Example function with loop:")
    print("  def count_to_5():")
    print("      for i in range(1, 6):")
    print("          print(i)")
    print("  count_to_5()  # Prints 1 to 5")
    print("-"*34)

def sais():
    print("\n" + "*"*26)
    print("QUESTION: Python Quiz (Answer with a, b, or c)")
    print("*"*26)
    print("ANSWER: Let's play!")
    
    score = 0
    
    print("\nQ1: What is 2 + 2?")
    print("a) 3")
    print("b) 4")
    print("c) 5")
    ans1 = input("Your answer: ").strip().lower()
    if ans1 == 'b':
        print("Correct!")
        score += 1
    else:
        print("Wrong!. Answer is b) 4")
    
    print("\nQ2: What does 'print' do?")
    print("a) Add numbers")
    print("b) Show text")
    print("c) Make loops")
    ans2 = input("Your answer: ").strip().lower()
    if ans2 == 'b':
        print("Correct!")
        score += 1
    else:
        print("Wrong. Answer is b) Show text")
    
    print("\nQ3: What is a variable?")
    print("a) A type of loop")
    print("b) A box for data")
    print("c) A math symbol")
    ans3 = input("Your answer: ").strip().lower()
    if ans3 == 'b':
        print("Correct!")
        score += 1
    else:
        print("Wrong. Answer is b) A box for data")
    
    print("\nQ4: What is indentation?")
    print("a) A type of data")
    print("b) Spaces for code blocks")
    print("c) A loop type")
    ans4 = input("Your answer: ").strip().lower()
    if ans4 == 'b':
        print("Correct!")
        score += 1
    else:
        print("Wrong. Answer is b) Spaces for code blocks")
    
    print(f"\nYour score: {score}/4")
    print("*"*26)

def siete():
    print("\n" + "+"*25)
    print("QUESTION: Python Tips")
    print("+"*25)
    print("ANSWER:")
    print("- Practice every day to get better.")
    print("- Use online sites like Codecademy or freeCodeCamp.")
    print("- Read errors carefully; they help fix bugs.")
    print("- Start with small projects, like a calculator.")
    print("- Join Python communities on Reddit or Discord.")
    print("- Always save your code with .py extension.")
    print("+"*25)

def ocho():
    print("\n" + "~"*22)
    print("QUESTION: Fun Facts about Python")
    print("~"*22)
    print("ANSWER:")
    print("- Python is named after Monty Python, not the snake!")
    print("- It was first released in 1991.")
    print("- Python powers Instagram and YouTube.")
    print("- The language has a 'Zen of Python' with 19 rules.")
    print("- You can write Python on a phone with apps like Pydroid.")
    print("- Python has a mascot called the 'Python' (a snake).")
    print("~"*22)

def bug():
    while True:
        os.system("cls")
        menu()
        choice = input().strip()
        
        if choice == '1':
            uno()
        elif choice == '2':
            dosht()
        elif choice == '3':
            tresht()
        elif choice == '4':
            quatro()
        elif choice == '5':
            cinco()
        elif choice == '6':
            sais()
        elif choice == '7':
            siete()
        elif choice == '8':
            ocho()
        elif choice == '9':
            print("\n" + "="*30)
            print("You have chosen to exit the program.\nThank you for using the system and \ntaking the time to explore its feature.")
            print("Your interaction means a lot, and i hope the program \nwas helpful and easy to use.")
            print("If you ever need it again, i'll be right here.")
            print("Goodbye, and have a great day ahead!")
            print("="*30)
            break
        else:
            print("\n" + "="*30)
            print("Oops! Pick 1 to 9 only.")
            print("="*30)
        
        time.sleep(10)
        input("\nPress Enter to go back to menu...")

if __name__ == "__main__":

    bug()
